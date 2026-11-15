# Nearest-neighbor classification of arm poses
import math

# features: (wrist height above shoulder, wrist distance
# sideways from shoulder), in meters
examples = [((0.45, 0.05), "raise hand: stop"),
            ((0.50, 0.10), "raise hand: stop"),
            ((0.00, 0.60), "point: go there"),
            ((0.05, 0.55), "point: go there"),
            ((-0.50, 0.10), "arm down: no command"),
            ((-0.45, 0.05), "arm down: no command")]

def classify(feat):
    best = min(examples,
               key=lambda e: math.dist(feat, e[0]))
    return best[1], round(math.dist(feat, best[0]), 2)

for pose in [(0.40, 0.12), (0.02, 0.50), (-0.40, 0.20)]:
    label, dist = classify(pose)
    print(f"pose {pose} -> {label} (distance {dist})")
