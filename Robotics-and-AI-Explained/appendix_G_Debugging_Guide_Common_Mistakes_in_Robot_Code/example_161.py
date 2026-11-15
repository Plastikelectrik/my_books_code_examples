ticks_per_rev = 360
wheel_diameter_mm = 65
ticks, dt_s = 120, 0.05

# Wrong: the distance is still in millimeters
dist = ticks / ticks_per_rev * 3.1416 * wheel_diameter_mm
wrong = dist / dt_s
# Right: convert to meters first
d_m = dist / 1000
right = d_m / dt_s
print(f"wrong speed: {wrong:.3f} 'm/s'")
print(f"right speed: {right:.3f} m/s")
