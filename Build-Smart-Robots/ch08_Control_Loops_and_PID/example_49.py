class PID:
    def __init__(self, kp, ki, kd, out_min=-255,
                 out_max=255):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.out_min, self.out_max = out_min, out_max
        self.integral = 0.0
        self.prev_meas = None

    def reset(self):
        self.integral = 0.0
        self.prev_meas = None

    def update(self, setpoint, measurement, dt):
        error = setpoint - measurement
        # derivative on measurement: no "kick" when
        # the setpoint changes suddenly
        if self.prev_meas is None:
            d = 0.0
        else:
            d = -(measurement - self.prev_meas) / dt
        self.prev_meas = measurement
        new_i = self.integral + error * dt
        out = (self.kp * error + self.ki * new_i
               + self.kd * d)
        # anti-windup: only integrate if not saturated
        if self.out_min < out < self.out_max:
            self.integral = new_i
        return max(self.out_min, min(self.out_max, out))

if __name__ == "__main__":
    pid = PID(300, 600, 5)
    print(pid.update(0.5, 0.0, 0.1))   # first command
