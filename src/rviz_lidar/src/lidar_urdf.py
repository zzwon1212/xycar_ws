#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan, Range
from std_msgs.msg import Header

lidar_points = None
def lidar_callback(data):
    global lidar_points
    lidar_points = data.ranges

rospy.init_node('lidar')

rospy.Subscriber('scan', LaserScan, lidar_callback, queue_size=1)

pub1 = rospy.Publisher('scan1', Range, queue_size=1)
pub2 = rospy.Publisher('scan2', Range, queue_size=1)
pub3 = rospy.Publisher('scan3', Range, queue_size=1)
pub4 = rospy.Publisher('scan4', Range, queue_size=1)

msg = Range()
msg.header = Header()
msg.radiation_type = Range().ULTRASOUND
msg.min_range = 0.02
msg.max_range = 2.0
msg.field_of_view = (30.0 / 180.0) * 3.14

while not rospy.is_shutdown():
    # scan 토픽 도착할 때까지 기다리기
    if lidar_points == None:
        continue

    msg.header.stamp = rospy.Time.now()

    # Range 메시지에 헤더와 거리정보 채우기
    # scan1, 2, 3, 4 토픽 발행하기
    msg.header.frame_id = 'front'
    msg.range = lidar_points[90]
    pub1.publish(msg)

    msg.header.frame_id = 'right'
    msg.range = lidar_points[180]
    pub2.publish(msg)

    msg.header.frame_id = 'back'
    msg.range = lidar_points[270]
    pub3.publish(msg)

    msg.header.frame_id = 'left'
    msg.range = lidar_points[0]
    pub4.publish(msg)

    rospy.sleep(0.01)