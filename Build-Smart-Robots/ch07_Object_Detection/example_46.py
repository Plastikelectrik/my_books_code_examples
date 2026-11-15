from dataclasses import dataclass

@dataclass
class Detection:
    label: str
    score: float
    box: tuple          # (x, y, w, h) in pixels

def detect(frame):
    """Replace with a real model. Here: fixed output."""
    return [Detection("cup", 0.91, (210, 120, 40, 50)),
            Detection("person", 0.42, (20, 30, 80, 200)),
            Detection("cup", 0.38, (60, 140, 30, 40))]

def best(dets, label, min_score=0.5):
    good = [d for d in dets
            if d.label == label and d.score >= min_score]
    return max(good, key=lambda d: d.score,
               default=None)

target = best(detect(frame=None), "cup")
if target:
    x, y, w, h = target.box
    print(f"cup at center x={x + w // 2}, "
          f"score {target.score:.2f}")
else:
    print("no confident cup: keep searching")
