#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node(name='sender', anonymous=True)
pub = rospy.Publisher(name='my_topic', data_class=Int32)
rate = rospy.Rate(1000)
cnt = 1

while pub.get_num_connections() == 0:
    pass

while not rospy.is_shutdown():
    pub.publish(cnt)
    cnt += 1
    rate.sleep()