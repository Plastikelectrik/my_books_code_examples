import numpy as np

rng = np.random.default_rng(42)
true_cm = 50.0
n = 200
readings = true_cm + rng.normal(0, 1.5, n)
# 5 % of readings are wild outliers
bad = rng.random(n) < 0.05
readings[bad] = rng.uniform(5, 400, bad.sum())

print("first 6:", np.round(readings[:6], 1))
print("mean:", round(readings.mean(), 1))
print("median:", round(np.median(readings), 1))
np.save("noisy.npy", readings)
