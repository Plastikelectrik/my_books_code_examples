# Label connected regions with a flood fill
import numpy as np

mask = np.zeros((8, 12), dtype=bool)
mask[1:3, 1:4] = True       # object 1
mask[4:7, 6:9] = True       # object 2
mask[1:2, 9:11] = True      # object 3

labels = np.zeros(mask.shape, dtype=int)
count = 0
for r in range(mask.shape[0]):
    for c in range(mask.shape[1]):
        if mask[r, c] and labels[r, c] == 0:
            count += 1
            stack = [(r, c)]
            while stack:
                y, x = stack.pop()
                inside = (0 <= y < mask.shape[0]
                          and 0 <= x < mask.shape[1])
                if (inside and mask[y, x]
                        and not labels[y, x]):
                    labels[y, x] = count
                    stack += [(y+1, x), (y-1, x),
                              (y, x+1), (y, x-1)]
print("objects found:", count)
for k in range(1, count + 1):
    print(f"object {k}: {np.sum(labels == k)} pixels")
