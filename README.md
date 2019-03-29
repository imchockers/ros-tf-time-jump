# ros-tf-time-jump
This is being used to refresh old tf frames that are being replayed from a rosbag file, so that they are properly processed by Rviz.

Simply encapsulate the file inside a ros package and add it to your workspace, then run the script as shown:
'''bash
rosrun time_jump time_jump.py
'''
Now that it is running, you need to remap the bag files to publish on 'tf_old' instead of 'tf', this can be done with:
'''bash
rosbag play <bag file> /tf:=tf_old
'''
time_jump will then subscribe to tf_old and republish the frames with current timestamps on tf.
