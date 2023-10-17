#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int32

def callback(msg):
    rospy.loginfo(msg.data)

rospy.init_node('receiver')
rospy.loginfo('Init')

rospy.Subscriber('msg_to_receiver', String, callback=callback)

pub = rospy.Publisher('ok_sign', data_class=Int32, queue_size=1)

while pub.get_num_connections() != 4:
    pass

for i in range(1, 5):
    pub.publish(i)
    rospy.sleep(1)

rospy.spin()