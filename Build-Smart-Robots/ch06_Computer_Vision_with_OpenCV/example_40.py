# Calibration: a 6.5 cm ball at 50 cm looks 90 px wide
REAL_CM = 6.5
f_px = 90 * 50 / REAL_CM          # focal length (px)
print(f"focal length: {f_px:.0f} px")

for width_px in [180, 90, 45, 30]:
    d = REAL_CM * f_px / width_px
    print(f"ball {width_px:3d} px wide -> {d:5.1f} cm")
