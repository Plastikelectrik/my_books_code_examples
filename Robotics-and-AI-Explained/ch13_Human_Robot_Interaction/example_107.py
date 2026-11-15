# Trust rises slowly with successes, drops after failures
import random

random.seed(16)
trust = 0.5                 # 0 = none, 1 = complete
reliability = 0.95       # succeeds 95% of the time
for day in range(1, 31):
    success = random.random() < reliability
    if success:
        trust += 0.05 * (1 - trust)       # slow growth
    else:
        trust -= 0.30 * trust             # sharp drop
    if day % 5 == 0 or not success:
        event = "ok" if success else "FAILURE"
        print(f"day {day:2d}: {event:7s} "
              f"trust {trust:.2f}")
