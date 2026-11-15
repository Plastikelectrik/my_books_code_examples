speed = 0.5                       # m/s
for rate_hz in [10, 50]:
    dt = 1 / rate_hz
    pos_wrong = pos_right = 0.0
    for _ in range(rate_hz):      # one second of loops
        pos_wrong += speed        # wrong: ignores dt
        pos_right += speed * dt   # right
    print(f"{rate_hz} Hz: wrong {pos_wrong:5.1f} m, "
          f"right {pos_right:.1f} m")
