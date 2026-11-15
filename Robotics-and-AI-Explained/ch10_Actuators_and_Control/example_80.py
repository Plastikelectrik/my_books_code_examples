# Average motor voltage for different PWM duty cycles
supply = 12.0                    # volts
for duty in [0, 25, 50, 75, 100]:
    avg = supply * duty / 100
    print(f"duty {duty:3d}% -> average {avg:4.1f} V")
