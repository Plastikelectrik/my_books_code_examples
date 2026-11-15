class PID:
    def __init__(self, kp, ki, kd, dt, limit=12.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.dt, self.limit = dt, limit
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, error):
        deriv = (error - self.prev_error) / self.dt
        self.prev_error = error
        trial = self.integral + error * self.dt
        out = (self.kp * error + self.ki * trial
               + self.kd * deriv)
        if abs(out) < self.limit:
            self.integral = trial      # safe to add
        out = (self.kp * error + self.ki * self.integral
               + self.kd * deriv)
        return max(-self.limit, min(self.limit, out))

pid = PID(0.15, 0.6, 0.001, dt=0.01)
for _ in range(500):
    pid.update(400.0)          # target out of reach
print(f"integral stays small: {pid.integral:.2f}")
