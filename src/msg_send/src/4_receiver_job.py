#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

def callback(msg):
    pass

rospy.init_node(name='receiver', anonymous=True)
rospy.loginfo('Init')
sub = rospy.Subscriber(name='topic', data_class=Int32, callback=callback, queue_size=10000)
rospy.spin()