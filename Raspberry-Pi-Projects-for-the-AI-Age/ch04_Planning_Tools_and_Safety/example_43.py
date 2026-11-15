# Each device: (name, volts, amps typical, amps peak)
devices = [
    ("Raspberry Pi 5 + cooler", 5.0, 1.6, 3.0),
    ("NVMe SSD",                5.0, 0.4, 0.8),
    ("USB gamepads x2",         5.0, 0.2, 0.3),
    ("Monitor 19 inch",        12.0, 1.5, 2.0),
    ("Audio amplifier",        12.0, 0.5, 2.5),
]

def summary(devs, volts):
    sel = [d for d in devs if d[1] == volts]
    typ = sum(d[2] for d in sel)
    peak = sum(d[3] for d in sel)
    return typ, peak, typ * volts

for v in (5.0, 12.0):
    typ, peak, watts = summary(devices, v)
    margin = peak * 1.25            # 25 % safety margin
    print(f"{v:4.0f} V rail: typical {typ:.1f} A "
          f"({watts:.0f} W), peak {peak:.1f} A")
    print(f"   use a supply of at least {margin:.1f} A")
