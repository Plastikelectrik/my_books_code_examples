import numpy as np

rng = np.random.default_rng(1)
dt, n = 0.01, 3000                 # 30 s at 100 Hz
t = np.arange(n) * dt
true = 10 * np.sin(0.5 * t)        # tilt in degrees
rate = np.gradient(true, dt)

gyro = rate + 0.8 + rng.normal(0, 0.5, n)  # bias!
acc = true + rng.normal(0, 3.0, n)         # noisy

g_only, comp = 0.0, 0.0
g_hist, c_hist = [], []
beta = 0.98
for i in range(n):
    g_only += gyro[i] * dt
    comp = beta * (comp + gyro[i] * dt) \
        + (1 - beta) * acc[i]
    g_hist.append(g_only)
    c_hist.append(comp)

def rms(x):
    return np.sqrt(np.mean((np.array(x) - true) ** 2))

print(f"gyro only:      {rms(g_hist):5.2f} deg error")
print(f"accel only:     {rms(acc):5.2f} deg error")
print(f"complementary:  {rms(c_hist):5.2f} deg error")
