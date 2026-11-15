# Ray casting: is the robot inside the forbidden zone?
def inside(point, polygon):
    x, y = point
    result = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            t = (y - y1) / (y2 - y1)
            x_cross = x1 + t * (x2 - x1)
            if x < x_cross:
                result = not result
    return result

stairs = [(4, 0), (6, 0), (6, 3), (5, 4), (4, 3)]
for pos in [(1, 1), (5, 1), (5.5, 3.2), (6.5, 2)]:
    zone = "FORBIDDEN -> stop" if inside(pos, stairs) \
        else "allowed"
    print(pos, zone)
