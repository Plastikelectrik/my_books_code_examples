# Complementary filter: smooth and drift-free tilt
import numpy as np

rng = np.random.default_rng(2)
dt, bias = 0.01, 0.2
true_angle = 10.0               # robot tilted 10 deg
gyro_only = fused = 0.0
for t in range(1, 3001):        # 30 seconds
    gyro = 0.0 + bias + rng.normal(0, 0.5)
    accel = true_angle + rng.normal(0, 3.0)  # noisy
    gyro_only += gyro * dt
    fused = 0.98 * (fused + gyro * dt) + 0.02 * accel
    if t % 1000 == 0:
        print(f"{t * dt:3.0f} s: gyro only "
              f"{gyro_only:6.2f}, fused {fused:6.2f} deg")
