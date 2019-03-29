#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Adapted from https://gist.github.com/wkentaro/2b38d8eb914c729197c6

import rospy
from tf2_msgs.msg import TFMessage
from jsk_recognition_msgs.msg import BoundingBoxArray
import message_filters


def cb_1(msg):
    global first_stamp, now
    now = rospy.Time.now()
    for i, tf in enumerate(msg.transforms):
        if first_stamp is None:
            first_stamp = tf.header.stamp
        tf.header.stamp -= first_stamp
        tf.header.stamp += now
    pub_1.publish(msg)


def cb_2(msg):
    global first_stamp, now
    if first_stamp is None:
        first_stamp = msg.header.stamp
    msg.header.stamp -= first_stamp
    msg.header.stamp += now
    for i, box in enumerate(msg.boxes):
        box.header.stamp -= first_stamp
        box.header.stamp += now
    pub_2.publish(msg)


rospy.init_node('hoge')
first_stamp = None

rospy.sleep(1)


pub_1 = rospy.Publisher('/tf', TFMessage, queue_size=1)

sub_1 = rospy.Subscriber('/tf_old', TFMessage, cb_1)

rospy.spin()
