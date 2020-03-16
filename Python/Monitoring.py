
import rospy
from diagnostic_msgs.msg import KeyValue
from diagnostic_msgs.msg import DiagnosticArray
from sensor_msgs.msg import Temperature
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState

cont_v = 0.0
cont_I = 0.0
pub_1 = rospy.Publisher('firmware/PowerSource/virtual/Batt_05', BatteryState, queue_size=10)
pub_2 = rospy.Publisher('firmware/PowerSource/virtual/Batt_12', BatteryState, queue_size=10)
pub_3 = rospy.Publisher('firmware/PowerSource/virtual/Batt_24', BatteryState, queue_size=10)
pub_4 = rospy.Publisher('firmware/PowerSource/Battery', BatteryState, queue_size=10)
msg_1 = BatteryState()
msg_2 = BatteryState()
msg_3 = BatteryState()
msg_4 = BatteryState()


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

def command_deco(num):
    switcher = {
        0:          '0',
        1:          'I_5',
        2:          'I_12',
        3:          'I_24',
        4:          'I_Batt',
        5:          'V_5',
        6:          'V_12',
        7:          'V_24',
        8:          'V_Batt',
        9:          'T_',
        10:         'T_',
        11:         'T_',
        12:         'T_',
        13:         'H',
        14:         'e',
        15:         'f'
    }
    data = switcher.get(num, '0')
    return data

def Hex2data(message):
    if message[0]=='$':
        # print message
        message2 = message.split('$')
        try:
            data_doc = int(message2[1])
            msg_1.header.stamp = rospy.Time.now()
            msg_2.header.stamp = rospy.Time.now()
            msg_3.header.stamp = rospy.Time.now()
            msg_4.header.stamp = rospy.Time.now()
            command =   0x00F & (data_doc>>16);
            data1 =     0x00F & (data_doc>>12);
            data2 =     0x00F & (data_doc>>8);
            checksum =  0x0FF & (data_doc);
            data1_hex =     int2hex(data1)
            data2_hex =     int2hex(data2)
            # print (command,data1,data2,checksum)
            if command<9:
                if (command+data1+data2)!=checksum:
                    if (command+data1+data2+5)==checksum:
                        data_str = data1_hex+data2_hex
                        data = float(data_str,16)
                    else:
                        data = 0
                else:
                    data_h = int(data1_hex,16)
                    data_l = int(data2_hex,16)
                    data_str = str(data_h)+'.'+str(data_l)
                    data = float(data_str)
                # print data_str
                # print data
                type_value = command_deco(command)
                # print type_value
                if type_value == 'V_5':
                    msg_1.voltage = data
                elif type_value == 'V_12':
                    msg_2.voltage = data
                elif type_value == 'V_24':
                    msg_3.voltage = data
                elif type_value == 'V_Batt':
                    msg_4.voltage = data
                elif type_value == 'I_5':
                    msg_1.current = data
                elif type_value == 'I_12':
                    msg_2.current = data
                elif type_value == 'I_24':
                    msg_3.current = data
                elif type_value == 'I_Batt':
                    msg_4.current = data
                elif type_value == 'T_':
                    print 'hola'
                elif type_value == 'H':
                    print 'hola'
                # print type_value+' = '+str(data)
                pub_1.publish(msg_1)
                pub_2.publish(msg_2)
                pub_3.publish(msg_3)
                pub_4.publish(msg_4)

        except:
            pass

def data2Hex(message):
    pub = rospy.Publisher('Serial_out', String, queue_size=10)
    message2 = message.split('-')
    switcher1 = {
	"sys":	    '0',
	"memo":	    'a',
        "vn300":    '1',
        "M8":       '2',
        "cam":      '3',
	"fuzz":	    '4'
    }
    switcher2 = {
	"on_24":	'1',
	"off_12":	'2',
	"0ff_24":	'3',
	"RAM_E1":	'1',
	"RAM_E2":	'2',
	"ROM_E1":	'6',
	"ROM_E2":	'7',
	"ROM_E3":	'8',
        "NC":       '1',
        "start":    '2',
        "<25":      '3',
        "<50":      '4',
        "<75":      '5',
        ">75":      '6',
        "work":     '7',
	"T1":	'c',
	"T2":	'd',
	"T3":	'e',
	"T4":	'f'
    }
    dato1 = switcher1.get(message2[0], "0")
    dato2 = switcher2.get(message2[1], "0")
    checksum_int = int(dato1,16)+int(dato2,16)
    checksum1 = int2hex(checksum_int/16)
    checksum2 = int2hex(checksum_int%16)
    string = dato1+dato2+checksum1+checksum2
    info = int(string,16)
    serial_message = str(info)
#    print serial_message
    pub.publish(serial_message)

class listener:
    def __init__(self):
        self.T_core0 = 0
        self.T_core1 = 0
        self.T_core2 = 0
        self.T_core3 = 0
	self.cont_vn300 = 0
	self.flag_vn300 = True
        self.listener()

    def vn300_callback(self,data):
	if self.cont_vn300 == 10:
	        percentage = int(data.value)
	        if percentage<25:
	            data2Hex('vn300-<25')
	        elif percentage<50:
	            data2Hex('vn300-<50')
	        elif percentage<75:
	            data2Hex('vn300-<75')
	        elif percentage<100:
	            data2Hex('vn300->75')
	        elif percentage==100:
		    if self.flag_vn300 == True:
	            	data2Hex('vn300-work')
			self.flag_vn300 = False
		self.cont_vn300 = 0
	self.cont_vn300 = self.cont_vn300+1

    def serial_data(self,data):
        Hex2data(data.data)

    def T0_callback(self,data):
        if abs(data.temperature) < 80:
            self.T_core0 = data.temperature
        else:
            self.T_core0 = 0

    def T1_callback(self,data):
        if abs(data.temperature) < 80:
            self.T_core1 = data.temperature
        else:
            self.T_core1 = 0

    def T2_callback(self,data):
        if abs(data.temperature) < 80:
            self.T_core2 = data.temperature
        else:
            self.T_core2 = 0

    def T3_callback(self,data):
        if abs(data.temperature) < 80:
            self.T_core3 = data.temperature
        else:
            self.T_core3 = 0
        T_core_avg = (self.T_core0 + self.T_core1 + self.T_core2 + self.T_core3)/4.0
	# Fussy control
	a = 0.25*T_core_avg-5.75
	b = 0.25*T_core_avg-7.0
	c = 0.25*T_core_avg-8.25
#	print T_core_avg
#	print (a,b,c)
	if a<0.0:
		a = 0.0
	elif a>1.0:
		a = 1.0
	if b<0.0:
		b = 0.0
	elif b>1.0:
		b = 1.0
	if c<0.0:
		c = 0.0
	elif c>1.0:
		c = 1.0
#	print(a,b,c)
	r = a+b+c
	if r==0.0:
		message = 'fuzz-T1'
	elif r<=1.0:
		message = 'fuzz-T2'
	elif r<=2.0:
		message = 'fuzz-T3'
	else:
		message = 'fuzz-T4'
#	print r
#	print message
	data2Hex(message)
        # print [self.T_core0, self.T_core1, self.T_core2, self.T_core3]
#        print T_core_avg

    def core_idle_callback(self,data):
        Idle0 = data.status[0].values[0].value
        Idle1 = data.status[1].values[0].value
        Idle2 = data.status[2].values[0].value
        Idle3 = data.status[3].values[0].value
        # print [Idle0, Idle1, Idle2, Idle3]

    def HDD_callback(self,data):
        HDD_availble = data.status[0].values[0].value
#        print HDD_availble
	data = HDD_availble.split('G')
	try:
		HDD_data = float(data[0])
#		print HDD_data
		if HDD_data <= 10:
			data2Hex("memo-ROM_E3")
		elif HDD_data <= 30:
			data2Hex("memo-ROM_E2")
		elif HDD_data <= 50:
			data2Hex("memo-ROM_E1")
	except:
		pass
#	print float(HDD_aviable)

    def RAM_callback(self,data):
        Physical_mem = data.status[0].values[0].value
        Swap_mem = data.status[1].values[0].value
	data1 = Physical_mem.split('M')
	data2 = Swap_mem.split('M')
	try:
		memo_used = float(data1[0])+float(data2[0])
#      		print [Physical_mem, Swap_mem]
#		print [memo_used]
		if memo_used > 7000:
			data2Hex("memo-RAM_E2")
		elif memo_used > 6000:
			data2Hex("memo-RAM_E1")
	except:
		pass

    def listener(self):
        rospy.init_node('Monitoring', anonymous=False)
        rospy.Subscriber('vectornav/ConnStatus', KeyValue, self.vn300_callback)
        rospy.Subscriber('Serial', String, self.serial_data)
        rospy.Subscriber('Resources/Core/0/Temperature', Temperature, self.T0_callback)
        rospy.Subscriber('Resources/Core/1/Temperature', Temperature, self.T1_callback)
        rospy.Subscriber('Resources/Core/2/Temperature', Temperature, self.T2_callback)
        rospy.Subscriber('Resources/Core/3/Temperature', Temperature, self.T3_callback)
        rospy.Subscriber('Resources/Core/Idle', DiagnosticArray, self.core_idle_callback)
        rospy.Subscriber('Resources/HDD', DiagnosticArray, self.HDD_callback)
        rospy.Subscriber('Resources/RAM', DiagnosticArray, self.RAM_callback)
        rospy.spin()

if __name__ == '__main__':
    my_list = listener()
