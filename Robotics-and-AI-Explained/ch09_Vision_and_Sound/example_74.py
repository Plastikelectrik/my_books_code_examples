# Two cameras 12 cm apart, focal length 700 px
f, B = 700, 0.12
for d in [84, 42, 21, 8, 2]:
    z = f * B / d
    print(f"disparity {d:3d} px -> depth {z:6.2f} m")
