import math

wheel_radius_m = 0.033      # 33 mm wheel
speed_m_s = 0.20            # forward speed
turn_deg = 90
turn_rad = math.radians(turn_deg)

circumference_m = 2 * math.pi * wheel_radius_m
rev_per_s = speed_m_s / circumference_m
print(f"Wheel turns {rev_per_s:.2f} times per second")
print(f"90 degrees is {turn_rad:.4f} radians")
