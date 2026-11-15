# Sense-think-act loop for a robot driving to a wall
distance = 100.0  # distance to wall in cm
speed = 15.0      # cm per step

for step in range(1, 11):
    # SENSE: read the distance sensor
    reading = distance
    # THINK: decide what to do
    if reading > 20:
        action = "forward"
    else:
        action = "stop"
    # ACT: change the world
    if action == "forward":
        distance = distance - speed
    print(f"step {step}: {reading:5.1f} cm -> {action}")
    if action == "stop":
        break
