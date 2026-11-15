import matplotlib.pyplot as plt

class Motor:
    def __init__(self):
        self.speed, self.load = 0.0, 0.0
    def step(self, pwm, dt):
        pwm = max(-255, min(255, pwm))
        eff = max(0, abs(pwm) - 40)
        tgt = (1 if pwm >= 0 else -1) * eff * 0.01
        tgt -= self.load
        self.speed += (tgt - self.speed) * dt / 0.15
        return self.speed

class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i, self.prev = 0.0, None
    def update(self, sp, meas, dt):
        e = sp - meas
        d = 0 if self.prev is None else \
            -(meas - self.prev) / dt
        self.prev = meas
        ni = self.i + e * dt
        out = self.kp * e + self.ki * ni + self.kd * d
        if -255 < out < 255:
            self.i = ni
        return max(-255, min(255, out))

dt, steps = 0.02, 300               # 6 s at 50 Hz
configs = {"P": (300, 0, 0), "PI": (150, 1500, 0),
           "PID": (150, 1500, 6)}
for name, gains in configs.items():
    m, pid, v = Motor(), PID(*gains), 0.0
    ts, vs = [], []
    for k in range(steps):
        t = k * dt
        m.load = 0.15 if t >= 3.0 else 0.0
        v = m.step(pid.update(0.5, v, dt), dt)
        ts.append(t)
        vs.append(v)
    peak, dip = max(vs[:150]), min(vs[150:])
    print(f"{name:3s}: peak {peak:.3f}  dip {dip:.3f}"
          f"  final {vs[-1]:.3f} m/s")
    plt.plot(ts, vs, label=name)
plt.axhline(0.5, ls="--", c="gray")
plt.xlabel("time (s)")
plt.ylabel("speed (m/s)")
plt.legend()
plt.savefig("pid_compare.png", dpi=120)
