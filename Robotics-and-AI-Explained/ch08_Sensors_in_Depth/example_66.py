# Estimate a constant distance from noisy readings
import numpy as np

rng = np.random.default_rng(5)
true_d = 2.00                   # meters
measurements = true_d + rng.normal(0, 0.10, 20)

x, P = 0.0, 1.0       # estimate and its variance
Q, R = 0.0001, 0.10 ** 2        # process and sensor noise
for i, z in enumerate(measurements, start=1):
    P = P + Q                   # predict
    K = P / (P + R)             # Kalman gain
    x = x + K * (z - x)         # update estimate
    P = (1 - K) * P             # update uncertainty
    if i in (1, 2, 5, 10, 20):
        print(f"step {i:2d}: z={z:.3f} -> estimate "
              f"{x:.3f} (K={K:.2f})")
