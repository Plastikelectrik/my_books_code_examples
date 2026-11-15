import random

state = "FORWARD"
timer = 0

def read_distance_cm():
    # Simulated sensor: sometimes an obstacle appears
    return random.choice([120, 90, 60, 25, 15, 80])

random.seed(3)
for step in range(15):
    d = read_distance_cm()
    if state == "FORWARD":
        if d < 30:
            state, timer = "BACKUP", 2
    elif state == "BACKUP":
        timer -= 1
        if timer == 0:
            state, timer = "TURN", 3
    elif state == "TURN":
        timer -= 1
        if timer == 0:
            state = "FORWARD"
    print(f"step {step:2d}  dist {d:3d} cm  -> {state}")
