import rospy
from std_msgs.msg import String
import serial
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
        self.serial_message = ""
        self.cont = 0
        self.ser.open()
        self.talker()

    def send_serial(self,data):
	L = len(data.data)
	info = data.data
	message = ''
	if L<5:
		for i in range(5-L):
			message = message+'0'
	print message+info
        self.serial_message = '$'+message+info+'\n'
	self.ser.write(self.serial_message)
#	print data.data

    def talker(self):
        pub = rospy.Publisher('Serial', String, queue_size=10)
        rospy.init_node('Firmware', anonymous=False)
        rate = rospy.Rate(10) # 2hz
        rospy.Subscriber('Serial_out', String, self.send_serial)
        while not rospy.is_shutdown():
#            if self.cont == 10:
#                print self.serial_message
#                self.ser.write(self.serial_message)
#                self.cont = 0
            str_in = self.ser.readline()
            if len(str_in)>0:
                rospy.loginfo(str_in)
                pub.publish(str_in)
            self.cont = self.cont + 1
            rate.sleep()

if __name__ == '__main__':
    my_list = listener()
