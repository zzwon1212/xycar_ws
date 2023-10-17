#!/usr/bin/env python

import rospy
from msg_send.msg import custom_msg

def callback(msg):
	print("1. Name: ", msg.last_name + msg.first_name)
	print("2. ID: ", msg.id_number)
	print("3. Phone Number: ", msg.phone_number)

rospy.init_node('msg_receiver', anonymous=True)

sub = rospy.Subscriber('msg_to_xycar', custom_msg, callback)

rospy.spin()