# Joint angles to reach a point, with a check
import math

L1, L2 = 0.30, 0.20

def inverse(x, y, elbow_up=True):
    d2 = x * x + y * y
    c2 = (d2 - L1**2 - L2**2) / (2 * L1 * L2)
    if abs(c2) > 1:
        return None                     # out of reach
    t2 = math.acos(c2)
    if elbow_up:
        t2 = -t2
    t1 = math.atan2(y, x) - math.atan2(
        L2 * math.sin(t2), L1 + L2 * math.cos(t2))
    return math.degrees(t1), math.degrees(t2)

def forward(a1, a2):
    t1, t2 = math.radians(a1), math.radians(a2)
    return (L1*math.cos(t1) + L2*math.cos(t1+t2),
            L1*math.sin(t1) + L2*math.sin(t1+t2))

for target in [(0.35, 0.20), (0.10, 0.40), (0.60, 0.0)]:
    sol = inverse(*target)
    if sol is None:
        print(target, "-> out of reach")
        continue
    x, y = forward(*sol)
    print(f"{target} -> angles ({sol[0]:.1f}, "
          f"{sol[1]:.1f}) check ({x:.2f}, {y:.2f})")
