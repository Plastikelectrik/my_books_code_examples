# Integrate rotation rate with a small constant bias
import numpy as np

rng = np.random.default_rng(1)
dt = 0.01                       # 100 readings per second
bias = 0.2                      # degrees per second error
angle = 0.0
for t in range(1, 6001):        # 60 seconds, robot still
    rate = 0.0 + bias + rng.normal(0, 0.5)
    angle += rate * dt
    if t % 1500 == 0:
        print(f"after {t * dt:4.0f} s: "
              f"angle {angle:5.2f} deg")
