#!/usr/bin/env python

import rospy
from msg_send.msg import custom_msg

rospy.init_node('msg_sender', anonymous=True)
pub = rospy.Publisher('msg_to_xycar', custom_msg)

msg = custom_msg()
msg.first_name = "gildon"
msg.last_name = "Hong"
msg.id_number = 20041003
msg.phone_number = "010-8990-3003"

rate = rospy.Rate(1)
while not rospy.is_shutdown():
	pub.publish(msg)
	print("sending message")
	rate.sleep()