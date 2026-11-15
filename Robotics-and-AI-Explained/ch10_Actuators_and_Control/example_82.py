# The load increases at t=1 s; who keeps the speed?
dt, tau, gain = 0.01, 0.2, 25.0
target = 100.0                    # desired rad/s

def simulate(closed_loop):
    speed, volts = 0.0, target / gain
    for i in range(1, 201):
        load = 30.0 if i * dt >= 1.0 else 0.0
        if closed_loop:
            error = target - speed
            volts = 0.15 * error + target / gain
        final = gain * volts - load
        speed += (final - speed) * dt / tau
    return speed

print(f"open loop  : {simulate(False):5.1f} rad/s")
print(f"closed loop: {simulate(True):5.1f} rad/s")
