import math

PERIOD = 1.2                          # s per step cycle
#        (offset, amplitude, phase in degrees)
GAIT = {"hip_L":  (90, 25, 0),
        "hip_R":  (90, 25, 0),
        "foot_L": (90, 20, 90),
        "foot_R": (90, 20, 90)}

def angles(t):
    out = {}
    for name, (off, amp, ph) in GAIT.items():
        a = 2 * math.pi * t / PERIOD + math.radians(ph)
        out[name] = off + amp * math.sin(a)
    return out

print("  t    hipL  hipR footL footR")
for k in range(7):
    t = k * PERIOD / 6
    a = angles(t)
    print(f"{t:4.2f}  " + "  ".join(
        f"{a[n]:5.1f}" for n in GAIT))
