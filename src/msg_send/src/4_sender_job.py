#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

rospy.init_node(name='sender', anonymous=True)
pub = rospy.Publisher(name='topic', data_class=Int32, queue_size=0)
rate = rospy.Rate(5)

def do_job(num):
    for i in range(num):
        i += 1
        pub.publish(i)

while pub.get_num_connections() == 0:
    pass

while not rospy.is_shutdown():
    num = input("The number of sending msg: ")
    rate.sleep() # 메시지 모두 처리한 후에 input을 다시 받도록 순서 유지

    start_all = rospy.get_time()
    for i in range(5):
        start_one = rospy.get_time()
        do_job(num)
        end_one = rospy.get_time()
        rate.sleep()
        sleep_one = rospy.get_time()

        print '---------------------------------'
        print 'spend_time:', round(end_one - start_one, 4) # 1, 2, ..., n까지 한 번씩 보내는 데 걸린 시간
        print 'sleep_time:', round(sleep_one - end_one, 4) # 0.2초 - spend_time
    end_all = rospy.get_time()

    print '---------------------------------'
    print 'total time:', round(end_all - start_all, 4) # 5번 반복하는 데 걸린 시간. 1초여야 정상
    print '---------------------------------'