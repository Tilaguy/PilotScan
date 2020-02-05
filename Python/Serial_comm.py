import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    timeout = 0,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS
)

def send_serial(data):
#    print data
    serial_message = '$'+data.data+'\n'
    ser.write(serial_message)
        
def talker():
    pub = rospy.Publisher('Serial', String, queue_size=10)
    rospy.init_node('Serial_comm', anonymous=False)
    rate = rospy.Rate(0.5) # 1hz
    rospy.Subscriber('Serial_out', String, send_serial)
    while not rospy.is_shutdown():
        
#        rospy.Subscriber('Serial_out', String, send_serial)
        try:
            ser.open()
            str_in = ser.readline()
            if len(str_in)>0:
                rospy.loginfo("serial red")
#                rospy.loginfo(str_in)
                pub.publish(str_in)
            ser.close()
        except:
            rospy.loginfo("serial did not read")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass