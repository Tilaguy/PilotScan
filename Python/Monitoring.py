import rospy
from diagnostic_msgs.msg import KeyValue
from std_msgs.msg import String

def int2hex(num):
    switcher = {
        0:          '0',
        1:          '1',
        2:          '2',
        3:          '3',
        4:          '4',
        5:          '5',
        6:          '6',
        7:          '7',
        8:          '8',
        9:          '9',
        10:         'a',
        11:         'b',
        12:         'c',
        13:         'd',
        14:         'e',
        15:         'f'
    }
    data_hex = switcher.get(num, '0')
    return data_hex
    
def Hex2data(message):
    if message[0]=='$':
        print message
        message2 = message.split('$')
        data_doc = int(message2[1])
        command =   0x00F & (data_doc>>16);
        data1 =     0x00F & (data_doc>>12);
        data2 =     0x00F & (data_doc>>8);
        checksum =  0x0FF & (data_doc);
        print (command,data1,data2,checksum)
        if (command+data1+data2)!=checksum:
            if (command+data1+data2+5)==checksum:
                command_hex =   int2hex(command)
                data1_hex =     int2hex(data1)
                data2_hex =     int2hex(data2)
                checksum_hex =  int2hex(checksum)
                data_str = data1_hex+data2_hex
                print data_str
                data = int(data_str,16)
            else:
                command = 0
                data1 = 0
                data2 = 0
        else:
            command_hex =   int2hex(command)
            data1_hex =     int2hex(data1)
            data2_hex =     int2hex(data2)
            checksum_hex =  int2hex(checksum)
            data_h = int(data1_hex,16)
            data_l = int(data2_hex,16)
            data_str = str(data_h)+'.'+str(data_l)
            print data_str
            data = float(data_str)
        print (command,data1,data2,checksum)
        print data
        
        

def data2Hex(message):
    pub = rospy.Publisher('Serial_out', String, queue_size=10)
    message2 = message.split('-')
    if message2[0]=="sys":
        switcher1 = {
            "sys":      '0'
        }
        switcher2 = {
            "on_24":    '1',
            "off_12":   '2',
            "off_24":   '3',
            "mem_E":    '4',
            "on_m8":    '5',
            "on_tty":   '6'
        }
    else:
        switcher1 = {
            "vn300":    '1',
            "M8":       '2',
            "cam":      '3'
        }
        switcher2 = {
            "NC":       '1',
            "start":    '2',
            "<25":      '3',
            "<50":      '4',
            "<75":      '5',
            ">75":      '6',
            "work":     '7'
        }
    switcher3 = {
        0:          '0',
        1:          '1',
        2:          '2',
        3:          '3',
        4:          '4',
        5:          '5',
        6:          '6',
        7:          '7',
        8:          '8',
        9:          '9',
        10:         'a',
        11:         'b',
        12:         'c',
        13:         'd',
        14:         'e',
        15:         'f'
    }
    dato1 = switcher1.get(message2[0], "0")
    dato2 = switcher2.get(message2[1], "0")
    checksum_int = int(dato1,16)+int(dato2,16)
    checksum1 = switcher3.get(checksum_int/16, "0")
    checksum2 = switcher3.get(checksum_int%16, "0")
    string = dato1+dato2+checksum1+checksum2
    info = int(string,16)
    serial_message = str(info)
    pub.publish(serial_message)

class listener:    
    def __init__(self):
        self.listener()
    
    def vn300_callback(self,data):
        percentage = int(data.value)
        if percentage<25:
            message = 'vn300-<25'
        elif percentage<50:
            message = 'vn300-<50'
        elif percentage<75:
            message = 'vn300-<75'
        elif percentage<100:
            message = 'vn300->75'
        elif percentage==100:
            message = 'vn300-work'
        data2Hex(message)
    
    def serial_data(self,data):
        Hex2data(data.data)
    
    def listener(self):
        rospy.init_node('Monitoring', anonymous=False)
        rospy.Subscriber('vectornav/ConnStatus', KeyValue, self.vn300_callback)
        rospy.Subscriber('Serial', String, self.serial_data)
        rospy.spin()

if __name__ == '__main__':
    my_list = listener()