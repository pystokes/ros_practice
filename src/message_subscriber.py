#!/usr/bin/env python

import rospy
from ros_practice.msg import Complex


def callback(msg):
    print 'Real:', msg.real
    print'Imaginary:', msg.imaginary
    print


rospy.init_node('message_subsciber')

sub = rospy.Subscriber('complex', Complex, callback)

rospy.spin()
