import rospy
import sys,os
from std_msgs.msg import String
from diagnostic_msgs.msg import KeyValue



class listener:
    def __init__(self):
        self.FLAG=0
        self.listener()

    def callback(self,data):
        status=float(data.value)
        if status == 100 and self.FLAG==0:
            self.FLAG=1
            rospy.loginfo("Lanching the data recorder.....")
            os.system('echo "recorder"')
            os.system('bash /home/harold/laun.sh')
            sys.exit(0)

    def listener(self):
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('launcher', anonymous=True)
        rospy.Subscriber('vectornav/ConnStatus', KeyValue, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    my_list = listener()
