import random
import time

distance = 100.0   # cm to the wall (the "world")

def sense():
    """Read the distance sensor (with noise)."""
    noise = random.uniform(-1.0, 1.0)
    return distance + noise

def think(reading):
    """Decide what to do."""
    if reading > 20:
        return "forward"
    return "stop"

def act(command):
    """Change the world."""
    global distance
    if command == "forward":
        distance -= 10   # we moved 10 cm closer
    print(f"{command:8s} -> wall at {distance:5.1f} cm")

for step in range(12):
    reading = sense()
    command = think(reading)
    act(command)
    time.sleep(0.1)
