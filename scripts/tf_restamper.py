#!/usr/bin/env python

# Code sourced from:
# https://answers.ros.org/question/11477/using-tf-data-from-bag-files/?answer=17152#post-id-17152
# Date: 7/4/2019

import roslib
import rospy
import tf
from tf2_msgs.msg import TFMessage

rospy.init_node("tf_restamper")
tfpublisher= rospy.Publisher("tf", TFMessage, queue_size=10)


def tfcallback(tfmessage):
    for transf in tfmessage.transforms:
        transf.header.stamp=rospy.Time.now()
    tfpublisher.publish(tfmessage)

tfproxy = rospy.Subscriber("tf_old", TFMessage, tfcallback)
rospy.spin()
