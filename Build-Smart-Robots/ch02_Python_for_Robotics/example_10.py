import math

class Robot:
    def __init__(self, x=0.0, y=0.0, theta=0.0):
        self.x = x
        self.y = y
        self.theta = theta   # heading in radians

    def move(self, v, w, dt):
        """Drive with speed v (m/s), turn rate w
        (rad/s) for dt seconds."""
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += w * dt

    def __repr__(self):
        deg = math.degrees(self.theta)
        return (f"Robot(x={self.x:.2f}, "
                f"y={self.y:.2f}, heading={deg:.0f})")

r = Robot()
r.move(v=0.5, w=0.0, dt=2.0)        # straight 1 m
r.move(v=0.0, w=math.pi / 2, dt=1)  # turn left 90
r.move(v=0.5, w=0.0, dt=2.0)        # straight 1 m
print(r)
