# Step-by-step algorithm for the minimum of a list
readings = [2.4, 1.8, 3.1, 0.9, 1.2, 2.7]   # meters

smallest = readings[0]
direction = 0
for i, d in enumerate(readings):
    if d < smallest:
        smallest = d
        direction = i
print(f"closest obstacle: {smallest} m "
      f"in direction {direction}")
print("check with min():", min(readings))
