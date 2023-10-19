#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from xycar_motor.msg import xycar_motor

msg_motor = xycar_motor()
distance = []

def callback_lidar(msg_scan):
    global distance, msg_motor

    distance = msg_scan.ranges

rospy.init_node('lidar_driver')
rospy.Subscriber('scan', LaserScan, callback_lidar, queue_size=1)
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
    obstacle = 0

    for degree in range(30, 150):
        if distance[degree] <= 0.3: # 30cm
            obstacle += 1
        if obstacle > 3:
            drive_stop()
            break

    if obstacle <= 3:
        drive_go()