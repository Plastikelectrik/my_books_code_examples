# Mark free and occupied cells along each ray
import math

W, H = 20, 12
world = [[0] * W for _ in range(H)]
for c in range(W):
    world[0][c] = world[H - 1][c] = 1
for r in range(H):
    world[r][0] = world[r][W - 1] = 1
for r in range(1, 9):
    world[r][12] = 1                # wall with a gap

known = [["?"] * W for _ in range(H)]
for rx, ry in [(4, 6), (8, 3)]:     # robot spots
    for a in range(0, 360, 4):
        dx = math.cos(math.radians(a))
        dy = math.sin(math.radians(a))
        for step in range(1, 40):
            cx = int(round(rx + dx * step * 0.5))
            cy = int(round(ry + dy * step * 0.5))
            if world[cy][cx] == 1:
                known[cy][cx] = "#"
                break
            known[cy][cx] = "."
for row in known:
    print("".join(row))
