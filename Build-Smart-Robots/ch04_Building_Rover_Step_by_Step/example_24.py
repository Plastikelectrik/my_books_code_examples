measured_m = 2.03          # tape measure
ticks_left = 3489
ticks_right = 3541
avg = (ticks_left + ticks_right) / 2
m_per_tick = measured_m / avg
print(f"meters per tick: {m_per_tick:.6f}")
print(f"left/right difference: "
      f"{100*(ticks_right-ticks_left)/avg:+.1f} %")
