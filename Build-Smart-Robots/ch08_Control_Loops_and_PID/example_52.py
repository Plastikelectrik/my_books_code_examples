import math

class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i, self.prev = 0.0, None
    def update(self, sp, meas, dt):
        e = sp - meas
        d = 0 if self.prev is None else \
            -(meas - self.prev) / dt
        self.prev = meas
        self.i += e * dt
        return self.kp * e + self.ki * self.i \
            + self.kd * d

# Wall along y = 0; robot starts 0.6 m away, angled
x, y, th = 0.0, 0.6, math.radians(10)
pid = PID(kp=10.0, ki=0.0, kd=8.0)  # a PD controller
TARGET = 0.30                     # keep 30 cm
dt, v = 0.05, 0.25
for k in range(161):
    dist = y                      # side sensor
    w = pid.update(TARGET, dist, dt)  # + = turn left
    w = max(-1.5, min(1.5, w))    # rad/s limit
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += w * dt
    if k % 40 == 0:
        print(f"t={k*dt:4.1f}s  distance={dist:.3f} m")
