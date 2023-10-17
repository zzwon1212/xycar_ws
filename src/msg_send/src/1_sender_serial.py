#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node(name='sender_serial')

pub = rospy.Publisher(name='my_topic', data_class=Int32, queue_size=1)

rate = rospy.Rate(1)

# 과제 '1. 데이터를 누락, 특히 처음과 끝' 해답
while pub.get_num_connections() != 3:
    pass

cnt = 1
while not rospy.is_shutdown():
    pub.publish(cnt)
    print('A')
    cnt += 1
    rate.sleep()