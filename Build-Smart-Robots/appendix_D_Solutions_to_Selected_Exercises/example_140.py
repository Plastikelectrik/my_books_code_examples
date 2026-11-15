import random

distance = 100.0

def sense(noise=5.0):
    return distance + random.uniform(-noise, noise)

def think(reading):
    if reading > 50:
        return 10            # cm per step
    if reading > 20:
        return 5
    return 0

random.seed(1)
for step in range(20):
    move = think(sense())
    distance -= move
    print(f"move {move:2d} cm -> wall "
          f"at {distance:5.1f} cm")
    if move == 0:
        break
