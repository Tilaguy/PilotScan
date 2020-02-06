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
        self.ser.open()
        self.talker()

    def send_serial(self,data):
    #    print data
        self.serial_message = '$'+data.data+'\n'

    def talker(self):
        pub = rospy.Publisher('Serial', String, queue_size=10)
        rospy.init_node('Firmware', anonymous=False)
        rate = rospy.Rate(0.5) # 1hz
        rospy.Subscriber('Serial_out', String, self.send_serial)
        while not rospy.is_shutdown():
            try:
                rospy.loginfo(self.serial_message)
                #ser.write(serial_message)
                rospy.sleep(0.01)
                str_in = ser.readline()
                if len(str_in)>0:
    #                rospy.loginfo("serial red")
                    rospy.loginfo(str_in)
                    pub.publish(str_in)
            except:
                #rospy.loginfo("serial did not read")
                #pass
                
            rate.sleep()

if __name__ == '__main__':
    my_list = listener()

#ser = serial.Serial(
#    port = '/dev/ttyUSB0',
#    baudrate = 9600,
#    timeout = 0,
#    parity = serial.PARITY_NONE,
#    stopbits = serial.STOPBITS_ONE,
#    bytesize = serial.EIGHTBITS
#)
#ser.close()
#serial_message = ""
#ser.open()
#
#def send_serial(data):
##    print data
#    serial_message = '$'+data.data+'\n'
#    
#        
#def talker():
#    pub = rospy.Publisher('Serial', String, queue_size=10)
#    rospy.init_node('Firmware', anonymous=False)
#    rate = rospy.Rate(0.5) # 1hz
#    rospy.Subscriber('Serial_out', String, send_serial)
#    while not rospy.is_shutdown():
#        try:
#            rospy.loginfo(serial_message)
#            #ser.write(serial_message)
#            rospy.sleep(0.01)
#            str_in = ser.readline()
#            if len(str_in)>0:
##                rospy.loginfo("serial red")
#                rospy.loginfo(str_in)
#                pub.publish(str_in)
#        except:
#            #rospy.loginfo("serial did not read")
#            #pass
#            
#        rate.sleep()
#
#if __name__ == '__main__':
#    try:
#        talker()
#    except rospy.ROSInterruptException:
#        pass
    
    
