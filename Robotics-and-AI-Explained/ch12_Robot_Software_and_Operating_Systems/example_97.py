# A typed message for a robot's position
from dataclasses import dataclass, asdict
import time

@dataclass
class Pose2D:
    x: float
    y: float
    theta: float          # heading in radians
    stamp: float = 0.0    # time of measurement

p = Pose2D(1.25, -0.40, 1.57, stamp=time.time())
print(p.x, p.y, p.theta)
print(sorted(asdict(p).keys()))
age = time.time() - p.stamp
print("message age below 1 s:", age < 1.0)
