# Reaction distance plus braking distance
def stopping_distance(speed, reaction_s, decel):
    reaction = speed * reaction_s
    braking = speed ** 2 / (2 * decel)
    return reaction + braking

for speed in [0.3, 0.8, 1.5, 2.0]:          # m/s
    d = stopping_distance(speed, reaction_s=0.2,
                          decel=1.0)       # m/s^2
    print(f"speed {speed:.1f} m/s -> stops within "
          f"{d:.2f} m")
