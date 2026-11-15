import random
from statistics import median, quantiles

random.seed(11)
samples = []  # (hour, latency in ms or None)
for i in range(24 * 12):     # every 5 minutes for a day
    hour = i / 12
    bad = 19 <= hour < 20    # evening congestion
    for _ in range(10):
        if random.random() < (0.08 if bad else 0.002):
            samples.append((hour, None))   # lost packet
        else:
            base = 45 if bad else 14
            ms = base + random.expovariate(0.3)
            samples.append((hour, ms))

def report(rows, label):
    ok = [ms for _, ms in rows if ms is not None]
    loss = 1 - len(ok) / len(rows)
    p95 = quantiles(ok, n=20)[-1]
    print(f"{label:9s} median {median(ok):5.1f} ms, "
          f"p95 {p95:5.1f} ms, loss {loss:.1%}")

report(samples, "all day")
report([s for s in samples if 19 <= s[0] < 20], "19-20 h")
report([s for s in samples
        if not 19 <= s[0] < 20], "other")
