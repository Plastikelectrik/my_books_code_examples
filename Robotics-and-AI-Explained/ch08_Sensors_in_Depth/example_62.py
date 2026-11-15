# Tilt angle from accelerometer x and z readings
import math

readings = [(0.00, 9.81), (1.70, 9.66),
            (4.90, 8.50), (6.94, 6.94)]   # (ax, az) m/s^2
for ax, az in readings:
    tilt = math.degrees(math.atan2(ax, az))
    print(f"ax={ax:4.2f} az={az:4.2f} -> "
          f"tilt {tilt:5.1f} deg")
