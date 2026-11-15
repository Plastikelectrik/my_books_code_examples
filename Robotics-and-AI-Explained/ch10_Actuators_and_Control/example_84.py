# Plot the speed for three different controllers
import matplotlib.pyplot as plt

dt, tau, gain, target = 0.01, 0.2, 25.0, 100.0

def run(kp, ki, kd):
    integ, prev, speed, out = 0.0, 0.0, 0.0, []
    for i in range(300):
        load = 30.0 if i * dt >= 1.5 else 0.0
        err = target - speed
        integ += err * dt
        u = kp * err + ki * integ + kd * (err - prev) / dt
        prev = err
        u = max(-12, min(12, u))
        speed += (gain * u - load - speed) * dt / tau
        out.append(speed)
    return out

plt.figure(figsize=(5, 3))
for label, g in [("P", (0.15, 0, 0)),
                 ("PI", (0.15, 0.6, 0)),
                 ("PID", (0.15, 0.6, 0.002))]:
    y = run(*g)
    plt.plot([i * dt for i in range(300)], y, label=label)
    print(f"{label:3s}: final speed {y[-1]:6.1f}")
plt.axhline(target, ls="--", c="gray")
plt.xlabel("time (s)")
plt.ylabel("speed (rad/s)")
plt.legend()
plt.tight_layout()
plt.savefig("pid_compare.png")
