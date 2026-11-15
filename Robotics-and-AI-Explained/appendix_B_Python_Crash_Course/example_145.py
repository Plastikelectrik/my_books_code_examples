import numpy as np

d = np.array([120, 95, 80, 40, 22])
print("in meters:", d / 100)
print("mean:", d.mean(), " std:", round(d.std(), 1))
print("close mask:", d < 50)
print("close values:", d[d < 50])

grid = np.zeros((3, 4))      # 3 rows, 4 columns
grid[1, 2] = 1               # mark one cell
print(grid)
print("shape:", grid.shape)
