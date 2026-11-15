import time

RATE_HZ = 20
period = 1 / RATE_HZ
next_time = time.monotonic()
for step in range(5):
    # read sensors, decide, send commands here
    print("cycle", step)
    next_time += period
    time.sleep(max(0.0, next_time - time.monotonic()))
