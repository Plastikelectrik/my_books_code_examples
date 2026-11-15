sudo apt install ros-lyrical-teleop-twist-keyboard
# Terminal 1 (on the Raspberry Pi)
ros2 run rover_bringup rover_bridge
# Terminal 2 (Pi or laptop on the same network)
ros2 run teleop_twist_keyboard teleop_twist_keyboard
