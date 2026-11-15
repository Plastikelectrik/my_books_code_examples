# Effect of a gearbox on speed and torque
motor_rpm = 6000       # motor speed, revolutions/minute
motor_torque = 0.05    # motor torque in newton-meters
efficiency = 0.85      # 85% of power reaches the output

for ratio in [1, 10, 50, 100]:
    out_rpm = motor_rpm / ratio
    out_torque = motor_torque * ratio * efficiency
    print(f"ratio {ratio:3d}:1 -> {out_rpm:7.1f} rpm, "
          f"{out_torque:5.2f} Nm")
