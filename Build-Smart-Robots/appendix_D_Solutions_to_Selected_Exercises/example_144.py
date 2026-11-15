def on_cmd(self, msg):
    forward = msg.linear.x > 0.0
    if forward and self.range_m < 0.25:
        msg.linear.x = 0.0          # block forward
        self.get_logger().warn("too close: stop")
    self.pub.publish(msg)
