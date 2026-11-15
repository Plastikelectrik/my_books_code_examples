# Visualize the distribution of noisy readings
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
readings = 50 + rng.normal(0, 2, size=1000)

plt.figure(figsize=(5, 3))
plt.hist(readings, bins=30)
plt.title("1000 readings of a 50 cm distance")
plt.xlabel("reading (cm)")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("histogram.png")
print("mean:", round(readings.mean(), 2))
print("std :", round(readings.std(), 2))
