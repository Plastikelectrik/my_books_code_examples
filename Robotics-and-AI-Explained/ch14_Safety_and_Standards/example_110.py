# Simplified separation distance for a mobile robot
def separation(v_robot, v_person=1.6, t_react=0.1,
               decel=1.0, margin=0.2):
    t_brake = v_robot / decel          # time to stop
    s_brake = v_robot ** 2 / (2 * decel)
    t_total = t_react + t_brake
    return (v_person * t_total + v_robot * t_react
            + s_brake + margin)

for v in [0.0, 0.5, 1.0, 1.5]:
    print(f"robot {v:.1f} m/s -> keep at least "
          f"{separation(v):.2f} m")
