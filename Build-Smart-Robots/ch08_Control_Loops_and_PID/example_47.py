class Motor:
    def __init__(self, gain=0.01, tau=0.15,
                 dead=40, load=0.0):
        self.gain = gain    # m/s per PWM unit
        self.tau = tau      # time constant (s)
        self.dead = dead    # PWM needed to move
        self.load = load    # extra friction (m/s)
        self.speed = 0.0

    def step(self, pwm, dt):
        pwm = max(-255, min(255, pwm))
        if abs(pwm) < self.dead:
            target = 0.0
        else:
            sign = 1 if pwm > 0 else -1
            eff = abs(pwm) - self.dead
            target = sign * (eff * self.gain - self.load)
        err = target - self.speed
        self.speed += err * dt / self.tau
        return self.speed

m = Motor()
for t in range(6):
    v = m.step(150, 0.1)
    print(f"t={0.1*(t+1):.1f}s speed={v:.3f} m/s")
