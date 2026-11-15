# Estimate runtime from a simple power budget
battery_voltage = 14.8    # volts
battery_capacity = 5.0    # amp-hours
usable = 0.8              # do not fully empty the battery

parts = {                 # average power in watts
    "computer": 8.0,
    "motors (driving)": 18.0,
    "lidar": 3.0,
    "camera": 2.0,
    "electronics": 1.5,
}
total_power = sum(parts.values())
energy_wh = battery_voltage * battery_capacity * usable

for name, watts in parts.items():
    share = watts / total_power * 100
    print(f"{name:17s} {watts:5.1f} W ({share:4.1f}%)")
print(f"total power: {total_power:.1f} W")
print(f"usable energy: {energy_wh:.1f} Wh")
print(f"runtime: {energy_wh / total_power:.2f} hours")
