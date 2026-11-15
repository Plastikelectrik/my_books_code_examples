# Keep the best box, drop boxes overlapping it a lot
def iou(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = ix * iy
    area = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / (area(a) + area(b) - inter)

dets = [((100, 100, 200, 200), 0.92),
        ((105, 102, 205, 198), 0.85),
        ((98, 95, 195, 205), 0.60),
        ((300, 120, 380, 210), 0.88)]
dets.sort(key=lambda d: -d[1])
kept = []
for box, score in dets:
    if all(iou(box, k[0]) < 0.5 for k in kept):
        kept.append((box, score))
for box, score in kept:
    print("keep", box, "score", score)
