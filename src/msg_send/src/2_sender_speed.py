#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

rospy.init_node(name='sender', anonymous=True)
pub = rospy.Publisher(name='long_string', data_class=String, queue_size=1)

rate = rospy.Rate(1)

pub_size = 1000000 # 1M
# pub_size = 5000000 # 5M
# pub_size = 10000000 # 10M
# pub_size = 20000000 # 20M
# pub_size = 50000000 # 50M

while pub.get_num_connections() == 0:
    pass

while not rospy.is_shutdown():
    pub.publish('#' * pub_size + ' ' + str(rospy.get_time()))
    rate.sleep()