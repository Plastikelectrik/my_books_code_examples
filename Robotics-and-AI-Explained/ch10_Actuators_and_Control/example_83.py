# PID keeps the speed at 100 rad/s despite the load
dt, tau, gain = 0.01, 0.2, 25.0

class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, error):
        self.integral += error * dt
        deriv = (error - self.prev_error) / dt
        self.prev_error = error
        return (self.kp * error + self.ki * self.integral
                + self.kd * deriv)

pid = PID(kp=0.15, ki=0.6, kd=0.001)
speed, target = 0.0, 100.0
for i in range(1, 301):
    load = 30.0 if i * dt >= 1.0 else 0.0
    volts = max(-12, min(12, pid.update(target - speed)))
    speed += (gain * volts - load - speed) * dt / tau
    if i in (25, 50, 100, 110, 150, 300):
        print(f"t={i * dt:.2f} s: speed {speed:6.1f}, "
              f"volts {volts:5.2f}")
