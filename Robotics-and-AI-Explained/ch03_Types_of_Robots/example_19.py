# Check hover thrust and payload for a quadcopter
g = 9.81
frame_kg = 1.2
battery_kg = 0.5
max_thrust_per_motor_n = 9.0   # newtons
motors = 4

def check(payload_kg):
    mass = frame_kg + battery_kg + payload_kg
    weight_n = mass * g
    thrust_n = motors * max_thrust_per_motor_n
    ratio = thrust_n / weight_n
    hover = weight_n / thrust_n * 100
    print(f"payload {payload_kg:.1f} kg: T/W {ratio:.2f},"
          f" hover at {hover:.0f}% throttle")

for p in [0.0, 0.5, 1.0, 1.5]:
    check(p)
