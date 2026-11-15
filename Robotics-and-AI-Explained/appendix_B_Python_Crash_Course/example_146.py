import numpy as np
import matplotlib
matplotlib.use("Agg")          # save files, no window
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 50)
speed = 0.5 * (1 - np.exp(-t / 0.3))
plt.figure(figsize=(5, 3))
plt.plot(t, speed, label="speed")
plt.xlabel("time (s)")
plt.ylabel("speed (m/s)")
plt.legend()
plt.tight_layout()
plt.savefig("speed.png")
print("chart saved as speed.png")
