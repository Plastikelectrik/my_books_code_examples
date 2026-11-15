mkdir -p ~/rover_ws/src
cd ~/rover_ws/src
ros2 pkg create --build-type ament_python \
  rover_bringup --dependencies rclpy std_msgs \
  geometry_msgs nav_msgs sensor_msgs
