# Estimate distance to a known object (a 0.30 m box)
f_pixels = 600          # focal length from calibration
H = 0.30                # real height in meters

for h_pixels in [360, 180, 90, 45]:
    Z = f_pixels * H / h_pixels
    print(f"box appears {h_pixels:3d} px tall -> "
          f"{Z:.2f} m away")
