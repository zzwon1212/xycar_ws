#!/usr/bin/env python

import rospy
from msg_send.msg import custom_msg
from std_msgs.msg import String

rospy.init_node('student')
pub = rospy.Publisher('msg_to_xycar', custom_msg, queue_size=1)
rate = rospy.Rate(1)

msg = custom_msg()
msg.first_name = 'Gildong'
msg.last_name = 'Hong'
msg.age = 21
msg.score = 100
msg.phone_number = '010-1234-5678'
msg.id_number = 20239876

def callback(msg):
    rospy.loginfo(msg.data)

sub = rospy.Subscriber('msg_from_xycar', String, callback=callback)

while pub.get_num_connections() != 1:
    pass

while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()