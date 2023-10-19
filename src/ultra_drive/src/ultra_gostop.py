#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32MultiArray
from xycar_motor.msg import xycar_motor

msg_motor = xycar_motor()
distance = []

def callback_ultra(msg_ultra):
    global distance

    distance = msg_ultra.data

rospy.init_node('ultra_driver')
rospy.Subscriber('xycar_ultrasonic', Int32MultiArray, callback_ultra, queue_size=1)
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

def drive_go():
    global msg_motor
    msg_motor.speed = 5
    msg_motor.angle = 0
    pub.publish(msg_motor)

def drive_stop():
    global msg_motor
    msg_motor.speed = 0
    msg_motor.angle = 0
    pub.publish(msg_motor)

rospy.sleep(3)
# while distance == []:
    # pass

while not rospy.is_shutdown():
    # 0 < 거리 < 10cm
    # 0은 무한대, 장애물이 없음을 의미
    if distance[2] > 0 and distance[2] <= 10:
        drive_stop()
    else:
        drive_go()

    # obstacle = False

    # if distance[2] > 0 and distance[2] <= 10:
    #     obstacle = True
    #     drive_stop()
    #     break

    # if obstacle == False:
    #     drive_go()