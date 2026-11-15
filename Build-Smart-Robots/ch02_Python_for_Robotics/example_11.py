import time

class Rate:
    """Keep a loop running at a fixed frequency."""
    def __init__(self, hz):
        self.period = 1.0 / hz
        self.next_t = time.monotonic()

    def sleep(self):
        self.next_t += self.period
        delay = self.next_t - time.monotonic()
        if delay > 0:
            time.sleep(delay)
        else:  # we are late: resynchronize
            self.next_t = time.monotonic()

rate = Rate(20)                 # 20 Hz
t0 = time.monotonic()
for i in range(40):
    _ = sum(range(20000))       # pretend to work
    rate.sleep()
elapsed = time.monotonic() - t0
print(f"40 cycles took {elapsed:.2f} s (target 2.00 s)")
