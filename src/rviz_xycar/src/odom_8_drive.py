#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from xycar_motor.msg import xycar_motor

msg_xycar_motor = xycar_motor()

rospy.init_node('driver')

pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

msg_xycar_motor.speed = 3

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    msg_xycar_motor.angle = -50
    for i in range(152):
        pub.publish(msg_xycar_motor)
        rate.sleep()

    msg_xycar_motor.angle = 0
    for i in range(30):
        pub.publish(msg_xycar_motor)
        rate.sleep()

    msg_xycar_motor.angle = 50
    for i in range(152):
        pub.publish(msg_xycar_motor)
        rate.sleep()

    msg_xycar_motor.angle = 0
    for i in range(30):
        pub.publish(msg_xycar_motor)
        rate.sleep()