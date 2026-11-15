def fan_speed(temp, running, on_at=50, off_at=45,
              full_at=70, min_duty=0.35):
    """Return the PWM duty cycle (0..1)."""
    if not running and temp < on_at:
        return 0.0
    if running and temp < off_at:
        return 0.0
    if temp >= full_at:
        return 1.0
    span = (temp - off_at) / (full_at - off_at)
    return round(max(min_duty, min(1.0, span)), 2)

running = False
for t in [40, 48, 52, 49, 46, 44, 60, 75]:
    duty = fan_speed(t, running)
    running = duty > 0
    print(f"{t:3d} °C -> duty {duty:4.2f}")
