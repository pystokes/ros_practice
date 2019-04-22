#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

# Initialize node
rospy.init_node('arm_robot_publisher')

# Define publishers
pub_joint1 = rospy.Publisher('/arm_robot/arm1_arm2_joint_position_controller/command', Float64, queue_size=10)
pub_joint2 = rospy.Publisher('/arm_robot/arm2_arm3_joint_position_controller/command', Float64, queue_size=10)

# Move
rate = rospy.Rate(3)
radian = 0
while not rospy.is_shutdown():

    # Fix the direction of arm2
    pub_joint1.publish(1)

    # Rotate arm3
    pub_joint2.publish(radian)

    radian += 0.1
    rate.sleep()
