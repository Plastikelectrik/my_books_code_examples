# Check every whole gear ratio from 1 to 100
motor_rpm, motor_torque, eff = 6000, 0.05, 0.85
valid = []
for ratio in range(1, 101):
    rpm = motor_rpm / ratio
    torque = motor_torque * ratio * eff
    if torque >= 3.0 and rpm >= 100:
        valid.append(ratio)
print("valid ratios:", valid)
need_power = 3.0 * 100 * 2 * 3.1416 / 60
print(f"output power needed: {need_power:.1f} W")
have = motor_torque * motor_rpm * 2 * 3.1416 / 60
print(f"motor power x eff : {have * eff:.1f} W")
