#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Int32

ok = 0
def callback(msg):
    global ok
    ok = msg.data

rospy.init_node('third')
pub = rospy.Publisher('msg_to_receiver', String, queue_size=1)

sub = rospy.Subscriber('ok_sign', Int32, callback=callback)

rate = rospy.Rate(1)

while ok != 3:
    pass

while not rospy.is_shutdown():
    pub.publish('3. Third')
    rate.sleep()
