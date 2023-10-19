#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
import tf
from math import sin, cos, tan
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from sensor_msgs.msg import Imu, JointState

# global Angle, Imudata
odom_quat = tf.transformations.quaternion_from_euler(0, 0, 0)

def callback_joint_states(msg_joint_states):
    global Angle
    Angle = msg_joint_states.position[msg_joint_states.name.index('front_left_hinge_joint')]

rospy.Subscriber('joint_states', JointState, callback_joint_states)

def callback_imu(msg_imu):
    global odom_quat
    odom_quat[0] = msg_imu.orientation.x
    odom_quat[1] = msg_imu.orientation.y
    odom_quat[2] = msg_imu.orientation.z
    odom_quat[3] = msg_imu.orientation.w

rospy.Subscriber('imu', Imu, callback_imu)

rospy.init_node('odom')

odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

# current_time = rospy.Time.now()
last_time = rospy.Time.now()
rate = rospy.Rate(30)
current_speed = 0.4
wheel_base = 0.2
x = 0
y = 0
yaw = 0
Angle = 0

while not rospy.is_shutdown():
    current_time = rospy.Time.now()
    # compute odometry in a typical way given the velocities of the robot
    dt = (current_time - last_time).to_sec()
    current_steering_angle = Angle
    current_angular_velocity = current_speed * tan(current_steering_angle) / wheel_base

    x_dot = current_speed * cos(yaw)
    y_dot = current_speed * sin(yaw)
    x += x_dot * dt
    y += y_dot * dt
    yaw += current_angular_velocity * dt

    # Odometry 정보를 차체에 해당하는 base_link에 연결
    # IMU 값에 따라 차체가 움직이게 하기 위해서
    odom_broadcaster.sendTransform(
        translation=(x, y, 0),
        rotation=odom_quat,
        time=current_time,
        child='base_link',
        parent='odom'
    )

    # next, we'll publish the odometry message over ROS
    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = 'odom'
    # set the pose (Position & Orientation)
    odom.pose.pose = Pose(Point(x, y, 0), Quaternion(*odom_quat))
    odom.child_frame_id = 'base_link'
    odom_pub.publish(odom)

    last_time = current_time
    rate.sleep()