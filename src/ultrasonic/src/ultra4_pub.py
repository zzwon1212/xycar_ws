#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 초음파 센서가 아두이노를 거쳐서 보낸 거리 정보를 토픽에 담아서 발행
import serial, rospy
from std_msgs.msg import Int32MultiArray

FRONT = [0, 0, 0, 0]

ser_front = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    )

def read_Sdata(s):
    s = s.strip()
    s_data = s.split("mm")
    s_data.remove('\r\n')
    s_data = list(map(int, s_data))
    return s_data

def read_sensor():
    sensor_data = ser_front.readline()
    ser_front.flushInput()
    ser_front.flushOutput()
    # ultrasonic_data = int(filter(str.isdigit, serial_data))
    FRONT = read_Sdata(sensor_data) # 문자열에서 거리값 4개 뽑아서 msg에 담기
    msg.data = FRONT

if __name__ == '__main__':

    rospy.init_node('ultra4_pub', anonymous=False) # initialize node
    pub = rospy.Publisher('ultra4', Int32MultiArray, queue_size=1)

    msg = Int32MultiArray() # message type
    while not rospy.is_shutdown():
        read_sensor()
        pub.publish(msg) # publish a message
        rospy.sleep(0.2)

    ser_front.close()