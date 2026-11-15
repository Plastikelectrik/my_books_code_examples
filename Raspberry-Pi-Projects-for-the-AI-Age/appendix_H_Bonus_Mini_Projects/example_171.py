from datetime import time

ON_FROM, ON_UNTIL = time(21, 0), time(6, 30)
HOLD_S = 90

def is_night(now):
    return now >= ON_FROM or now < ON_UNTIL

def brightness(now, seconds_since_motion):
    if not is_night(now) or seconds_since_motion > HOLD_S:
        return 0.0
    if seconds_since_motion > HOLD_S - 15:   # fade out
        return round((HOLD_S - seconds_since_motion)
                     / 15 * 0.4, 2)
    return 0.4  # soft, not full power

for now, since in [(time(14, 0), 5), (time(22, 30), 5),
                   (time(22, 30), 80), (time(3, 10), 95),
                   (time(6, 45), 1)]:
    print(f"{now:%H:%M} motion {since:3d} s ago -> "
          f"{brightness(now, since):.2f}")
