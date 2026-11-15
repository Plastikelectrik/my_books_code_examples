import math
import numpy as np

class World:
    def __init__(self):
        self.w, self.h = 4.0, 3.0           # room size m
        # obstacles as circles: (x, y, radius)
        self.obstacles = [(2.0, 1.5, 0.3),
                          (3.2, 0.6, 0.2)]

    def free(self, x, y):
        if not (0 < x < self.w and 0 < y < self.h):
            return False
        for ox, oy, r in self.obstacles:
            if math.hypot(x - ox, y - oy) < r:
                return False
        return True

    def ray(self, x, y, th, max_r=3.0, step=0.01):
        """Distance to the first hit along a ray."""
        for r in np.arange(0, max_r, step):
            px = x + r * math.cos(th)
            py = y + r * math.sin(th)
            if not self.free(px, py):
                return r
        return max_r

class SimRobot:
    def __init__(self, world, x, y, th):
        self.world = world
        self.x, self.y, self.th = x, y, th

    def sense(self):
        return self.world.ray(self.x, self.y, self.th)

    def act(self, v, w, dt):
        nx = self.x + v * math.cos(self.th) * dt
        ny = self.y + v * math.sin(self.th) * dt
        if self.world.free(nx, ny):     # no crashing
            self.x, self.y = nx, ny
        self.th += w * dt

world = World()
bot = SimRobot(world, 0.5, 1.5, 0.0)
for t in range(60):
    d = bot.sense()
    if d > 0.5:
        v, w = 0.3, 0.0        # forward
    else:
        v, w = 0.0, 1.2        # turn left
    bot.act(v, w, 0.1)
    if t % 10 == 0:
        print(f"t={t/10:3.1f}s pos=({bot.x:.2f},"
              f"{bot.y:.2f}) dist={d:.2f}")
