#!/usr/bin/env python
# license removed for brevity
import rospy
from diagnostic_msgs.msg import KeyValue

def talker():
    msgKey = KeyValue()
    msgKey.key = "ConnStatus[%]";
    pub1 = rospy.Publisher('vectornav/ConnStatus', KeyValue, queue_size=10)
    rospy.init_node('vectornav', anonymous=False)
    count = 0
    percentage = 0
    msgKey.value = 0
    flag = True
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msgKey.value = str(percentage)
        if count == 10:
            if (percentage<100) and (flag):
                percentage = percentage+1
#                print "hola"
                
            elif percentage>100 or not flag:
                flag = False
                percentage = percentage-1
                if percentage<1:
                    flag = True
                    
            count = 0
            
        count = count+1
        #rospy.loginfo(msgKey.value)
        pub1.publish(msgKey)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
