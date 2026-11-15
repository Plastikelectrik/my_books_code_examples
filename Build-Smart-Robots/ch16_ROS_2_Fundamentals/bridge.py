import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range
from tf2_ros import TransformBroadcaster
from rover_bringup.rover import Rover

def yaw_to_quat(yaw):
    return (0.0, 0.0, math.sin(yaw / 2),
            math.cos(yaw / 2))

class RoverBridge(Node):
    def __init__(self):
        super().__init__("rover_bridge")
        self.declare_parameter("port", "/dev/ttyACM0")
        self.declare_parameter("wheelbase", 0.15)
        self.declare_parameter("m_per_tick", 0.000578)
        port = self.get_parameter("port").value
        self.L = self.get_parameter("wheelbase").value
        self.k = self.get_parameter("m_per_tick").value
        self.bot = Rover(port)
        self.x = self.y = self.th = 0.0
        self.prev = None
        self.cmd = (0.0, 0.0)
        self.last_cmd = self.get_clock().now()
        self.odom_pub = self.create_publisher(
            Odometry, "odom", 10)
        self.range_pub = self.create_publisher(
            Range, "range", 10)
        self.tf = TransformBroadcaster(self)
        self.create_subscription(Twist, "cmd_vel",
                                 self.on_cmd, 10)
        self.create_timer(0.05, self.update)   # 20 Hz

    def on_cmd(self, msg):
        self.cmd = (msg.linear.x, msg.angular.z)
        self.last_cmd = self.get_clock().now()

    def update(self):
        now = self.get_clock().now()
        age = (now - self.last_cmd).nanoseconds / 1e9
        v, w = self.cmd if age < 0.5 else (0.0, 0.0)
        self.bot.velocity(v - w * self.L / 2,
                          v + w * self.L / 2)
        (tl, tr), dist, _ = self.bot.status()
        if self.prev is not None:
            dl = (tl - self.prev[0]) * self.k
            dr = (tr - self.prev[1]) * self.k
            d, dth = (dl + dr) / 2, (dr - dl) / self.L
            self.x += d * math.cos(self.th + dth / 2)
            self.y += d * math.sin(self.th + dth / 2)
            self.th += dth
        self.prev = (tl, tr)
        self.publish(now, v, w, dist)

    def publish(self, now, v, w, dist):
        q = yaw_to_quat(self.th)
        odom = Odometry()
        odom.header.stamp = now.to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"
        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        (odom.pose.pose.orientation.x,
         odom.pose.pose.orientation.y,
         odom.pose.pose.orientation.z,
         odom.pose.pose.orientation.w) = q
        odom.twist.twist.linear.x = v
        odom.twist.twist.angular.z = w
        self.odom_pub.publish(odom)

        t = TransformStamped()
        t.header = odom.header
        t.child_frame_id = "base_link"
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.rotation = odom.pose.pose.orientation
        self.tf.sendTransform(t)

        r = Range()
        r.header.stamp = odom.header.stamp
        r.header.frame_id = "sonar_link"
        r.radiation_type = Range.ULTRASOUND
        r.field_of_view = 0.26
        r.min_range, r.max_range = 0.02, 4.0
        r.range = dist / 100 if dist > 0 \
            else float("inf")
        self.range_pub.publish(r)

    def destroy_node(self):
        self.bot.close()
        super().destroy_node()

def main():
    rclpy.init()
    node = RoverBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == "__main__":
    main()
