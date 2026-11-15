ros2 node list                 # running nodes
ros2 topic list                # active topics
ros2 topic echo /chatter       # print messages
ros2 topic hz /chatter         # message rate
ros2 topic info /chatter       # type and connections
ros2 interface show geometry_msgs/msg/Twist
# publish a velocity command once
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.1}, angular: {z: 0.0}}"
