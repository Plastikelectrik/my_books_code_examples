from launch import LaunchDescription
from launch_ros.actions import Node

def robot(ns, port):
    return Node(package="rover_bringup",
                executable="rover_bridge",
                namespace=ns,
                parameters=[{"port": port}],
                output="screen")

def generate_launch_description():
    return LaunchDescription([
        robot("rover1", "/dev/ttyACM0"),
        robot("rover2", "/dev/ttyACM1"),
    ])
