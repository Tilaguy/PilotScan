import rospy
from diagnostic_msgs.msg import KeyValue
import serial

def Hex2data(message,serial_port):
    if message[0]=='$':
        print message
        message2 = message.split('$')
        data_str = message2[1]
        print data_str
        print int(data_str)
#    char dato1 = 0;
#	char dato2 = 0;
#	char checksum = 0;
#	char data_aux[5] = "00000";
#	unsigned int data_int = 0;
#	unsigned int i;
#	unsigned int n2 = 0;
#	if (data[0]=='$'){
#		//printf ("Recibido_dato = %s\n", data);
#		for (i=1; i<(n-1); i++){
#			data_aux[i] = data[i];
#		}
#		//printf ("Recibido_dato_aux = %s\n", data_aux);
#		data_int = atoi(data_aux);
#		//printf ("Recibido_dato = %d\n", data_int);
#		dato1 = 0x0F&(data_int>>12);
#		printf ("Recibido_dato1 = %x\n", dato1);
#		dato2 = 0x0F&(data_int>>8);
#		printf ("Recibido_dato2 = %x\n", dato2);
#		checksum = 0x0F&data_int;
#		if ((dato1+dato2)!=checksum)
#			data_int = 0;
#	}

def data2Hex(message,serial_port):
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
    serial_message = '$'+str(info)+'\n'
    serial_port.write(serial_message)

class listener:    
    def __init__(self):
        self.ser = serial.Serial(
            port = '/dev/ttyUSB0',
            baudrate = 9600,
            timeout = 0,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS
        )
        self.ser.close()
        self.ser.open()
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
        data2Hex(message,self.ser)
    
    def listener(self):
        rospy.init_node('dsPIC_Comm', anonymous=False)
        rospy.Subscriber('vectornav/ConnStatus', KeyValue, self.vn300_callback)
        rospy.spin()

if __name__ == '__main__':
    my_list = listener()