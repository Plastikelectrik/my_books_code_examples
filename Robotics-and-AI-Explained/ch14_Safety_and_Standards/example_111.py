# Stop if the controller stops sending heartbeats
TIMEOUT = 0.5                     # seconds
heartbeats = [0.0, 0.2, 0.4, 0.6, 0.8, 1.6, 1.8]
check_times = [0.3, 0.7, 1.0, 1.2, 1.4, 1.7, 1.9]

last = None
for t in check_times:
    last = max((h for h in heartbeats if h <= t),
               default=None)
    alive = last is not None and t - last <= TIMEOUT
    state = "running" if alive else "STOP MOTORS"
    print(f"t={t:.1f} s: last heartbeat "
          f"{last:.1f} s -> {state}")
