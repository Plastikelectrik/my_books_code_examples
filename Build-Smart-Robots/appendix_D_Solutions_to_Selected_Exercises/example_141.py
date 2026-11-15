import math
import numpy as np

class World:
    def __init__(self):
        self.w, self.h = 4.0, 3.0
        self.obstacles = [(2.0, 1.5, 0.3),
                          (3.2, 0.6, 0.2)]
    def free(self, x, y):
        if not (0 < x < self.w and 0 < y < self.h):
            return False
        return all(math.hypot(x - ox, y - oy) >= r
                   for ox, oy, r in self.obstacles)
    def ray(self, x, y, th, max_r=3.0, step=0.01):
        for r in np.arange(0, max_r, step):
            if not self.free(x + r * math.cos(th),
                             y + r * math.sin(th)):
                return r
        return max_r

world = World()
x, y, th = 0.5, 1.4, 0.0
A = math.radians(30)
path = []
for t in range(200):
    front = world.ray(x, y, th)
    left = world.ray(x, y, th + A)
    right = world.ray(x, y, th - A)
    if front > 0.5 and min(left, right) > 0.3:
        v, w = 0.3, 0.0
    else:
        v = 0.05
        w = 1.2 if left > right else -1.2
    nx = x + v * math.cos(th) * 0.1
    ny = y + v * math.sin(th) * 0.1
    if world.free(nx, ny):
        x, y = nx, ny
    th += w * 0.1
    path.append((x, y))
closest = min(min(math.hypot(px - ox, py - oy) - r
                  for ox, oy, r in world.obstacles)
              for px, py in path)
print(f"final position ({x:.2f}, {y:.2f})")
print(f"closest approach to an obstacle: {closest:.2f} m")
