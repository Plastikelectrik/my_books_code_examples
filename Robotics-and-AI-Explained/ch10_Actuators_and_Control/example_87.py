# Compare velocity profiles of two joint movements
start, end, T = 0.0, 90.0, 2.0     # degrees, seconds

def linear(t):
    return start + (end - start) * t / T

def cubic(t):
    s = t / T
    return start + (end - start) * (3 * s**2 - 2 * s**3)

dt = 0.25
print(" t    linear  cubic  cubic speed")
for k in range(9):
    t = k * dt
    v = (cubic(min(t + 0.01, T)) - cubic(t)) / 0.01
    print(f"{t:4.2f} {linear(t):7.1f} {cubic(t):6.1f} "
          f"{v:7.1f} deg/s")
