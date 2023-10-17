#!/usr/bin/env python

import rospy
import math
from xycar_motor.msg import xycar_motor
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

rospy.init_node('converter')

pub = rospy.Publisher('joint_states', JointState, queue_size=1)

msg_joint_states = JointState()
msg_joint_states.header = Header()
msg_joint_states.name = ['front_right_hinge_joint', 'front_left_hinge_joint',
                         'front_right_wheel_joint', 'front_left_wheel_joint',
                         'rear_right_wheel_joint','rear_left_wheel_joint']
msg_joint_states.velocity = []
msg_joint_states.effort = []

wheel = -3.14

def callback(msg_xycar_motor):
    global wheel, msg_joint_states, pub

    # msg_xycar_motor.speed
    steering = math.radians(msg_xycar_motor.angle * 0.4)

    if wheel > 3.14:
        wheel = -3.14
    else:
        wheel += 0.01

    msg_joint_states.header.stamp = rospy.Time.now()
    msg_joint_states.position = [steering, steering, wheel, wheel, wheel, wheel]

    pub.publish(msg_joint_states)

sub = rospy.Subscriber('xycar_motor', xycar_motor, callback=callback, queue_size=1)

rospy.spin()