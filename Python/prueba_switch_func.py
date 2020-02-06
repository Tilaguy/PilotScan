import rospy
import sys,os
from std_msgs.msg import String
from diagnostic_msgs.msg import KeyValue
import time
import serial

def data2Hex(message):
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
    print string
    print int(string,16)
    
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
        self.flag = False
        self.flag2 = False
        self.cont = 0
        self.data1 = 0
        self.data2 = 0
        self.ser.close()
        self.ser.open()
        print (ser.portstr)
        self.listener()

    def vn300_callback(self,data):
        string = "$"
    	if self.flag:
    		if not self.flag2:
    			self.data1 = 0x0
    			self.data2 = 0x1
    			print self.data1,self.data2
    			checksum = self.data1+self.data2
    			
    			print self.checksum
    			print "$1799"
    		self.ser.write("$1799\n")
    		self.cont = 0
    		self.flag = False
    	else:
    		a = self.ser.readline()
    		if len(a)>0:
    			print a
    			self.cont = self.cont+1
    			if self.cont == 10:
    				self.flag = True

    def listener(self):
        rospy.init_node('dsPIC_Comm', anonymous=False)
        rospy.Subscriber('vectornav/ConnStatus', KeyValue, self.vn300_callback)
        rospy.spin()

if __name__ == '__main__':
    my_list = listener()

data2Hex("cam-work")
