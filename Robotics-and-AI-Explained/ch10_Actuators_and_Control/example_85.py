# PD control of a joint angle (motor as integrator)
dt = 0.01
angle, velocity = 0.0, 0.0
target = 90.0                   # degrees
kp, kd = 40.0, 9.0
for i in range(1, 151):
    error = target - angle
    accel = kp * error - kd * velocity
    velocity += accel * dt
    angle += velocity * dt
    if i % 25 == 0:
        print(f"t={i * dt:.2f} s: angle {angle:6.2f} deg")
