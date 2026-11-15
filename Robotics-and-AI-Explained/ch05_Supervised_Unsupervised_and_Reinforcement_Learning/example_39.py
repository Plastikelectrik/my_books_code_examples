# Flag readings far from normal behavior
import numpy as np

rng = np.random.default_rng(4)
normal = rng.normal(1.0, 0.1, 500)    # vibration in g
mean, std = normal.mean(), normal.std()

new = np.array([1.05, 0.92, 1.48, 1.01, 0.62, 1.10])
z = (new - mean) / std          # how many std away
for value, score in zip(new, z):
    flag = "ANOMALY" if abs(score) > 3 else "ok"
    print(f"{value:.2f} g  z={score:+.1f}  {flag}")
