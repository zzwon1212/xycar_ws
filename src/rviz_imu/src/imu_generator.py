#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RVOZ 기반 IMU 뷰어 제작
import rospy
from sensor_msgs.msg import Imu
from tf.transformations import quaternion_from_euler

rospy.init_node('imu_generator')
pub = rospy.Publisher('imu', Imu, queue_size=1)

# imu_data.txt 파일에서 한 줄씩 읽어다가
file_path = '/home/jiwon/xycar_ws/src/rviz_imu/src/imu_data.txt'

rpy_all = []

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        rpy_one = []
        for part in parts:
            rpy_one.append(float(part.split(': ')[1]))
        rpy_all.append(rpy_one)

imuMSG = Imu()
imuMSG.header.frame_id = 'map'

rate = rospy.Rate(100)
seq = 0

for rpy_one in rpy_all:
    imuMSG.header.stamp = rospy.Time.now()
    imuMSG.header.seq = seq
    seq += 1

    quaternion = quaternion_from_euler(rpy_one[0], rpy_one[1], rpy_one[2])
    imuMSG.orientation.x = quaternion[0]
    imuMSG.orientation.y = quaternion[1]
    imuMSG.orientation.z = quaternion[2]
    imuMSG.orientation.w = quaternion[3]

    pub.publish(imuMSG)
    print(imuMSG)
    rate.sleep()