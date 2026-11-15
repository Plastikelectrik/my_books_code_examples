# Publishes a speed command every 0.5 seconds
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpeedPublisher(Node):
    def __init__(self):
        super().__init__("speed_publisher")
        self.pub = self.create_publisher(
            Twist, "/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.tick)

    def tick(self):
        msg = Twist()
        msg.linear.x = 0.2       # forward speed in m/s
        self.pub.publish(msg)
        self.get_logger().info("sent speed 0.2 m/s")

def main():
    rclpy.init()
    rclpy.spin(SpeedPublisher())

if __name__ == "__main__":
    main()
