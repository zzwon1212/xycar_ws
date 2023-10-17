#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def callback(data):
    s = "Location: %.2f, %.2f" % (data.x, data.y)
    rospy.loginfo(rospy.get_caller_id() + s)

rospy.init_node("my_listner", anonymous=True) # Generating subscriber object
rospy.Subscriber("/turtle1/pose", Pose, callback) # Calling func. when message is received
rospy.spin()