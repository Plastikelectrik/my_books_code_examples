import time

def slow_task():
    time.sleep(0.03)        # e.g. a network call

for name, extra in [("fast loop", False),
                    ("blocked", True)]:
    start = time.monotonic()
    for _ in range(10):
        if extra:
            slow_task()
    avg = (time.monotonic() - start) / 10 * 1000
    print(f"{name:9s}: {avg:5.1f} ms per cycle")
