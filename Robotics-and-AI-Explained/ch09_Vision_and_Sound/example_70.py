# Color mask, centroid and bounding box
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
img = rng.integers(90, 160, (120, 160, 3))
img = img.astype(np.uint8)
img[40:80, 95:135] = (210, 40, 35)          # red object

r = img[:, :, 0].astype(int)
g = img[:, :, 1].astype(int)
b = img[:, :, 2].astype(int)
mask = (r > 150) & (g < 90) & (b < 90)

rows, cols = np.nonzero(mask)
cy, cx = rows.mean(), cols.mean()
print("red pixels:", mask.sum())
print(f"centroid: x={cx:.1f}, y={cy:.1f}")
print("box: x", cols.min(), "-", cols.max(),
      " y", rows.min(), "-", rows.max())

fig, ax = plt.subplots(1, 2, figsize=(5.5, 2.2))
ax[0].imshow(img)
ax[0].set_title("camera image")
ax[1].imshow(mask, cmap="gray")
ax[1].plot(cx, cy, "r+", markersize=12)
ax[1].set_title("red mask + centroid")
for a in ax:
    a.axis("off")
plt.tight_layout()
plt.savefig("color_mask.png")
