# First-order model: speed approaches its final value
dt = 0.01               # seconds per step
tau = 0.20              # motor time constant (s)
gain = 25.0             # rad/s per volt at steady state
volts = 6.0
speed = 0.0
for i in range(1, 101):
    target = gain * volts
    speed += (target - speed) * dt / tau
    if i in (10, 20, 40, 60, 100):
        pct = speed / target * 100
        print(f"t={i * dt:.1f} s: {speed:6.1f} rad/s "
              f"({pct:4.1f}%)")
