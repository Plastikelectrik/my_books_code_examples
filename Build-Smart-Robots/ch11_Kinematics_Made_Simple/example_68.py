import math

L1, L2 = 0.12, 0.10        # link lengths (m)

def fk(t1, t2):
    x = L1 * math.cos(t1) + L2 * math.cos(t1 + t2)
    y = L1 * math.sin(t1) + L2 * math.sin(t1 + t2)
    return x, y

def ik(x, y, elbow_up=True):
    c2 = (x*x + y*y - L1*L1 - L2*L2) / (2 * L1 * L2)
    if abs(c2) > 1:
        return None                     # unreachable
    t2 = math.acos(c2)
    if elbow_up:
        t2 = -t2
    t1 = math.atan2(y, x) - math.atan2(
        L2 * math.sin(t2), L1 + L2 * math.cos(t2))
    return t1, t2

target = (0.15, 0.08)
for up in (True, False):
    t1, t2 = ik(*target, elbow_up=up)
    hx, hy = fk(t1, t2)
    name = "elbow up  " if up else "elbow down"
    print(f"{name}: t1={math.degrees(t1):6.1f} "
          f"t2={math.degrees(t2):6.1f} -> "
          f"({hx:.3f}, {hy:.3f})")
print("far target:", ik(0.30, 0.0))
