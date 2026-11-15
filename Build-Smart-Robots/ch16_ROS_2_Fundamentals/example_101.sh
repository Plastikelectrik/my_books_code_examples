ros2 bag record /odom /range /cmd_vel -o test_drive
ros2 bag info test_drive
ros2 bag play test_drive
