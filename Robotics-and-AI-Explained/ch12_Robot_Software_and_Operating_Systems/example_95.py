# Run a task at 20 Hz and measure the real timing
import time

RATE = 20                    # Hz
period = 1.0 / RATE
next_time = time.perf_counter()
times = []
for i in range(20):
    start = time.perf_counter()
    times.append(start)
    sum(range(20000))        # pretend work
    next_time += period
    sleep = next_time - time.perf_counter()
    if sleep > 0:
        time.sleep(sleep)

gaps = [b - a for a, b in zip(times, times[1:])]
avg_ms = sum(gaps) / len(gaps) * 1000
print(f"target period: {period * 1000:.1f} ms")
print(f"average period: {avg_ms:.1f} ms")
print(f"worst gap: {max(gaps) * 1000:.1f} ms")
