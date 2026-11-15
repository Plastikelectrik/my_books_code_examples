# Compare predicted boxes with the true box
def iou(a, b):
    # boxes as (x1, y1, x2, y2)
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    area = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / (area(a) + area(b) - inter)

truth = (100, 100, 200, 220)
for name, pred in [("good", (105, 98, 205, 215)),
                   ("shifted", (140, 130, 240, 250)),
                   ("wrong", (300, 50, 360, 120))]:
    score = iou(truth, pred)
    ok = "correct" if score >= 0.5 else "miss"
    print(f"{name:8s}: IoU {score:.2f} -> {ok}")
