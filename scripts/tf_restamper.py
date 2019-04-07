# Code sourced from:
# https://answers.ros.org/question/11477/using-tf-data-from-bag-files/?answer=17152#post-id-17152
# Date: 7/4/2019

import roslib
#roslib.load_manifest('tf')
import rospy
import tf

rospy.init_node("tf_restamper")
tfpublisher= rospy.Publisher("tf",tf.msg.tfMessage)


def tfcallback(tfmessage):
    for transf in tfmessage.transforms:
        transf.header.stamp=rospy.Time.now()
    tfpublisher.publish(tfmessage)

tfproxy = rospy.Subscriber("tf_old",tf.msg.tfMessage,tfcallback)
rospy.spin()