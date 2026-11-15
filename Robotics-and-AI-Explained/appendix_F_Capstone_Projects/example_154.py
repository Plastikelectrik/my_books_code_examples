import math
import random

random.seed(4)
SENSORS = [-0.02, -0.01, 0.0, 0.01, 0.02]  # meters

def line_y(x):                     # the line on the floor
    return 0.15 * math.sin(x / 0.6)

def read_sensors(x, y, th):
    values = []
    for s in SENSORS:
        sx = x + 0.05 * math.cos(th) + s * math.sin(th)
        sy = y + 0.05 * math.sin(th) - s * math.cos(th)
        d = abs(sy - line_y(sx))
        dark = math.exp(-(d / 0.012) ** 2)
        values.append(dark + random.gauss(0, 0.03))
    return values

def line_offset(values):
    w = [max(v, 0.0) for v in values]
    if sum(w) < 0.05:
        return None                  # line lost
    return sum(s * v for s, v in zip(SENSORS, w)) / sum(w)

x, y, th = 0.0, 0.0, 0.25
v, dt, kp, kd = 0.20, 0.02, 60.0, 2.0
prev, errors, lost = 0.0, [], 0
for step in range(600):
    off = line_offset(read_sensors(x, y, th))
    if off is None:
        lost += 1
        off = prev
    omega = -(kp * off + kd * (off - prev) / dt)
    omega = max(-6.0, min(6.0, omega))
    prev = off
    x += v * math.cos(th) * dt
    y += v * math.sin(th) * dt
    th += omega * dt
    errors.append(abs(y - line_y(x)))
    if step % 100 == 99:
        t = (step + 1) * dt
        print(f"t={t:4.1f} s  x={x:5.2f} m  "
              f"error={errors[-1] * 1000:5.1f} mm")
avg = sum(errors[100:]) / len(errors[100:])
print(f"mean error after 2 s: {avg * 1000:.1f} mm")
print(f"steps with line lost: {lost}")
