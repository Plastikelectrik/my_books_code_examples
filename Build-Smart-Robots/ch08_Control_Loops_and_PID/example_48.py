class Motor:
    def __init__(self, gain=0.01, tau=0.15, dead=40):
        self.gain, self.tau, self.dead = gain, tau, dead
        self.speed = 0.0

    def step(self, pwm, dt):
        pwm = max(-255, min(255, pwm))
        eff = max(0, abs(pwm) - self.dead)
        target = (1 if pwm >= 0 else -1) * eff * self.gain
        err = target - self.speed
        self.speed += err * dt / self.tau
        return self.speed

SETPOINT = 0.50      # m/s
for kp in [200, 500, 1000]:
    m, v = Motor(), 0.0
    for _ in range(250):         # 5 s at 50 Hz
        error = SETPOINT - v
        v = m.step(kp * error, 0.02)
    print(f"Kp={kp:5d}: final speed {v:.3f} m/s, "
          f"error {SETPOINT - v:+.3f}")
