cd ~/rover_ws
colcon build --symlink-install
source install/setup.bash
ros2 run rover_bringup talker
