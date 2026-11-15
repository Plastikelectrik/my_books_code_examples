from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="rover_bringup",
            executable="rover_bridge",
            name="rover_bridge",
            parameters=[{
                "port": "/dev/ttyACM0",
                "wheelbase": 0.154,
                "m_per_tick": 0.000578,
            }],
            output="screen",
        ),
    ])
