import numpy as np

rng = np.random.default_rng(5)
fs = 100
ax = rng.normal(0, 0.02, 1000)       # forward accel (g)
ax[300:303] += [-0.2, 0.15, -0.05]   # door threshold
ax[700:704] += [-1.2, -0.8, 0.3, 0.1]  # collision!

jerk = np.abs(np.diff(ax)) * fs       # g per second
THRESH = 60
events = np.where(jerk > THRESH)[0]
if events.size:
    first = events[0]
    print(f"collision at t={first / fs:.2f} s, "
          f"jerk {jerk[first]:.0f} g/s")
print("door threshold max jerk:",
      round(jerk[295:310].max()), "g/s")
