import math

class Odometry:
    def __init__(self, m_per_tick, wheelbase):
        self.k = m_per_tick
        self.L = wheelbase
        self.x = self.y = self.th = 0.0
        self.prev = None

    def update(self, ticks_left, ticks_right):
        if self.prev is None:
            self.prev = (ticks_left, ticks_right)
            return self.pose()
        dl = (ticks_left - self.prev[0]) * self.k
        dr = (ticks_right - self.prev[1]) * self.k
        self.prev = (ticks_left, ticks_right)
        d = (dr + dl) / 2
        dth = (dr - dl) / self.L
        mid = self.th + dth / 2
        self.x += d * math.cos(mid)
        self.y += d * math.sin(mid)
        self.th = math.atan2(math.sin(self.th + dth),
                             math.cos(self.th + dth))
        return self.pose()

    def pose(self):
        return self.x, self.y, self.th

if __name__ == "__main__":
    odo = Odometry(m_per_tick=0.000578, wheelbase=0.15)
    # Simulated readings: straight, then a left turn
    readings = [(0, 0), (1730, 1730), (1730, 2138),
                (3460, 3868)]
    for tl, tr in readings:
        x, y, th = odo.update(tl, tr)
        print(f"ticks ({tl:4d},{tr:4d}) -> x={x:.3f} "
              f"y={y:.3f} th={math.degrees(th):6.1f}")
