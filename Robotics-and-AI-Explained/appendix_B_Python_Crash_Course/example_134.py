def choose_action(distance_cm):
    if distance_cm < 20:
        return "stop"
    elif distance_cm < 50:
        return "slow down"
    else:
        return "drive"

for d in [10, 35, 120]:
    print(f"{d:4d} cm -> {choose_action(d)}")
