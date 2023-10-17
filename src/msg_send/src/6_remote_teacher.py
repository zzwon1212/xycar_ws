#!/usr/bin/env python

import rospy
from msg_send.msg import custom_msg
from std_msgs.msg import String
import time

name = None
def callback(msg):
    global name
    name = msg.first_name + ' ' + msg.last_name

rospy.init_node('teacher')
sub = rospy.Subscriber('msg_to_xycar', custom_msg, callback=callback, queue_size=1)

pub = rospy.Publisher('msg_from_xycar', String, queue_size=1)
rate = rospy.Rate(1)
current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

while name is None:
    pass

while not rospy.is_shutdown():
    # Good morning, Gildong Hong 2023-10-06 12:13:11
    pub.publish('Good morning, ' + name + ' ' + current_time)
    rate.sleep()

rospy.spin()