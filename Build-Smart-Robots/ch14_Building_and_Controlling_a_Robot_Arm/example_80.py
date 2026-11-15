import numpy as np

def min_jerk(a, b, T, rate=50):
    """Return a list of poses from a to b over T s."""
    a, b = np.array(a, float), np.array(b, float)
    n = max(2, int(T * rate))
    tau = np.linspace(0, 1, n)
    s = 10 * tau**3 - 15 * tau**4 + 6 * tau**5
    return [a + (b - a) * si for si in s]

traj = min_jerk([90, 90, 90], [135, 60, 140], T=1.5)
print("points:", len(traj))
for i in [0, 15, 37, 60, 74]:
    print(f"t={i/50:.2f}s ->", np.round(traj[i], 1))
speeds = np.abs(np.diff(np.array(traj), axis=0)) * 50
print("peak joint speed (deg/s):",
      np.round(speeds.max(axis=0), 1))
