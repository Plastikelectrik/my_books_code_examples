import math
import numpy as np

SENSOR_X = np.array([-0.03, -0.015, 0.0, 0.015, 0.03])
LINE_W = 0.019                         # 19 mm tape

def read_sensors(offset, rng):
    """Reflectance 0..1000: high = dark line."""
    d = np.abs(SENSOR_X - offset)
    dark = np.clip(1 - (d - LINE_W / 2) / 0.01, 0, 1)
    return 100 + 800 * dark + rng.normal(0, 20, 5)

def line_position(vals, lo=100, hi=900):
    n = np.clip((vals - lo) / (hi - lo), 0, 1)
    if n.sum() < 0.3:
        return None                    # line lost
    return float((n * SENSOR_X).sum() / n.sum())

def follow(kp, kd, speed=0.4, seconds=10, seed=0):
    rng = np.random.default_rng(seed)
    dt, offset, heading = 0.01, 0.01, 0.0
    prev, worst, lost = 0.0, 0.0, 0
    for k in range(int(seconds / dt)):
        t = k * dt
        curve = 2.5 * math.sin(0.6 * t)  # track bends
        pos = line_position(read_sensors(offset, rng))
        if pos is None:
            lost += 1
            pos = prev                    # remember side
        err = -pos
        w = kp * err + kd * (err - (-prev)) / dt
        prev = pos
        heading += (w - curve * speed) * dt
        offset += speed * math.sin(heading) * dt
        worst = max(worst, abs(offset))
    return worst, lost

for kp, kd in [(40, 0.0), (120, 0.0), (120, 1.5)]:
    worst, lost = follow(kp, kd)
    print(f"Kp={kp:3d} Kd={kd:3.1f}: max offset "
          f"{1000 * worst:5.1f} mm, lost {lost} steps")
