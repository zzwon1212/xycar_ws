#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def callback(msg):
    data = msg.data.split(' ')
    size = len(data[0])
    time = rospy.get_time() - float(data[1])
    # 과제 '2. 데이터 크기에 따른 전송 속도' 해답: 강의에서는 20MB가 적절한 것으로 보인다고 했으나 나는 큰 차이를 체감하지 못함
    rospy.loginfo(str(size/1000000) + 'MB, ' + str(round(time, 4)) + 's, ' + str(round(size/time/1000000, 2)) + 'mbps')

rospy.init_node(name='receiver', anonymous=True)
rospy.loginfo('Init')
sub = rospy.Subscriber(name='long_string', data_class=String, callback=callback)
rospy.spin()