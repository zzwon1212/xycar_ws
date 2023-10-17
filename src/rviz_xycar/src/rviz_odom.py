#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Converter 노드가 보내는 /joint_states 토픽을 받아서 바퀴의 방향과 회전 속도 정보를 획득하고
# 그 정보를 바탕으로 오도메트리 데이터를 만들어 /odom 토픽에 담아 발행한다.

import rospy
from nav_msgs.msg import Odometry
import tf
from math import sin, cos, pi
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from sensor_msgs.msg import JointState

rospy.init_node('rviz_odom')

pub = rospy.Publisher('odom', Odometry, queue_size=1)
odom_broadcaster = tf.TransformBroadcaster()

x = 0.0
y = 0.0
th = 0.0

vx = 0.1
vy = -0.1
vth = 0.1

last_time = rospy.Time.now()

rate = rospy.Rate(1)

def callback(msg_joint_states):
    global last_time, th, x, y # TODO 더 좋은 방법?
    current_time = rospy.Time.now()

    vth = msg_joint_states.position[0]

    dt = (current_time - last_time).to_sec()
    delta_x = (vx * cos(th) - vy * sin(th)) * dt
    delta_y = (vx * sin(th) + vy * cos(th)) * dt
    delta_th = vth * dt

    x += delta_x
    y += delta_y
    th += delta_th

    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    odom_broadcaster.sendTransform(
        translation=(x, y, 0.0),
        rotation=odom_quat,
        time=current_time,
        child='base_link',
        parent='odom'
    )

    msg_odom = Odometry()
    msg_odom.header.stamp = current_time
    msg_odom.header.frame_id = 'odom'
    msg_odom.pose.pose = Pose(position=Point(x, y, 0.0), orientation=Quaternion(*odom_quat))
    msg_odom.twist.twist = Twist(linear=Vector3(vx, vy, 0), angular=Vector3(0, 0, vth))

    pub.publish(msg_odom)

    last_time = current_time

sub = rospy.Subscriber('joint_states', JointState, callback=callback, queue_size=1)

rospy.spin()