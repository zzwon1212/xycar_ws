#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

# cnt = 0
def callback(msg):
    # global cnt
    # cnt += 1
    # if msg.data == cnt:
    #     print(msg.data)
    # else:
    #     print('Fail: msg = {}, cnt = {}'.format(msg.data, cnt))
    print(msg.data)

rospy.init_node(name='receiver_serial')
sub = rospy.Subscriber(name='my_topic', data_class=Int32, callback=callback, queue_size=1)

rospy.spin()