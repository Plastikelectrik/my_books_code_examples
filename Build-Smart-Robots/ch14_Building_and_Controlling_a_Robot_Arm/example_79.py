import math

L1, L2 = 0.105, 0.110      # upper arm, forearm (m)
SHOULDER_H = 0.07          # shoulder height above table

# Servo calibration: servo = sign * math_deg + offset
CAL = {"base": (1, 90), "shoulder": (1, 0),
       "elbow": (1, 180)}

def to_servo(name, rad):
    sign, off = CAL[name]
    return sign * math.degrees(rad) + off

def ik3(x, y, z):
    base = math.atan2(y, x)
    r = math.hypot(x, y)
    h = z - SHOULDER_H
    c2 = (r*r + h*h - L1*L1 - L2*L2) / (2 * L1 * L2)
    if abs(c2) > 1:
        return None
    t2 = -math.acos(c2)                  # elbow up
    t1 = math.atan2(h, r) - math.atan2(
        L2 * math.sin(t2), L1 + L2 * math.cos(t2))
    return (to_servo("base", base),
            to_servo("shoulder", t1),
            to_servo("elbow", t2))

for target in [(0.15, 0.0, 0.05), (0.10, 0.10, 0.02),
               (0.12, -0.08, 0.10), (0.04, 0.0, 0.0),
               (0.30, 0.0, 0.0)]:
    sol = ik3(*target)
    if sol is None:
        print(f"{target}: out of reach")
    else:
        b, sh, el = sol
        print(f"{target}: base {b:5.1f} "
              f"shoulder {sh:5.1f} elbow {el:5.1f}")
