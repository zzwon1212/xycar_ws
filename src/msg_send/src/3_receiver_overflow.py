#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.sleep(1)
    rospy.loginfo(msg.data)

rospy.init_node(name='receiver', anonymous=True)
rospy.loginfo('Init')
# 과제 '3. (너무 많이 보내서) 도착한 데이터를 처리 불가' 해답
sub = rospy.Subscriber(name='my_topic', data_class=Int32, callback=callback, queue_size=10000)
rospy.spin()