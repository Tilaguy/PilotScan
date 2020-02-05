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
ser.close()
ser.open()

def callback(data):
    print data
#    serial_message = '$'+data+'\n'
#    serial_port.write(serial_message)
        
def talker():
    pub = rospy.Publisher('Serial', String, queue_size=10)
    rospy.init_node('Serial_comm', anonymous=False)
    rospy.Subscriber('dsPIC_Comm', String, callback)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        str_in = ser.read_line()
        if len(str_in)>0:
            rospy.loginfo(str_in)
            pub.publish(str_in)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass