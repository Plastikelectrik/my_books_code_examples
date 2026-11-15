import numpy as np

RES = 0.05                       # 5 cm per cell
W, H = 4.0, 3.0                  # room size (m)
grid = np.zeros((int(H / RES), int(W / RES)),
                dtype=np.uint8)

def add_box(grid, x0, y0, x1, y1):
    """Mark a rectangle (meters) as occupied."""
    r0, r1 = int(y0 / RES), int(y1 / RES)
    c0, c1 = int(x0 / RES), int(x1 / RES)
    grid[r0:r1, c0:c1] = 1

grid[0, :] = grid[-1, :] = 1     # walls
grid[:, 0] = grid[:, -1] = 1
add_box(grid, 1.0, 0.0, 1.2, 2.0)    # wall piece
add_box(grid, 2.4, 1.0, 2.6, 3.0)    # another one
add_box(grid, 3.0, 0.4, 3.5, 0.7)    # a box
np.save("room.npy", grid)
print("grid shape:", grid.shape)
print("occupied cells:", int(grid.sum()))
