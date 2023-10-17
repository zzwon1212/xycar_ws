#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_node', anonymous=True) # Making node
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # Generating publisher object

msg = Twist()
msg.linear.x = rospy.get_param('~circle_size')
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 1.8

# Publishing messages at a 1Hz frequency
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()
