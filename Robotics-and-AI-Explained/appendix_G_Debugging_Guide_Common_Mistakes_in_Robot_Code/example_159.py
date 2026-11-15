import math

angle_deg = 90
print("wrong:", round(math.sin(angle_deg), 3))
rad = math.radians(angle_deg)
print("right:", round(math.sin(rad), 3))
print("back to degrees:", math.degrees(math.pi / 2))
