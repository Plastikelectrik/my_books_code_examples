import numpy as np
import cv2
from astar import astar          # previous example

grid = np.load("room.npy")
RES = 0.05
robot_radius_m = 0.12            # half width + margin
r_cells = int(np.ceil(robot_radius_m / RES))
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE, (2 * r_cells + 1,
                        2 * r_cells + 1))
inflated = cv2.dilate(grid, kernel)
print("occupied before:", int(grid.sum()),
      "after:", int(inflated.sum()))
path, n = astar(inflated, (10, 5), (50, 74))
print("safe path found:", path is not None,
      "| cells:", len(path))
np.save("inflated.npy", inflated)
