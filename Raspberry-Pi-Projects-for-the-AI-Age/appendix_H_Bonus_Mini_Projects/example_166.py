import math, random
from statistics import mean

random.seed(5)
day = []  # (minute, temp, humidity)
for minute in range(0, 24 * 60, 10):
    hour = minute / 60
    a = (hour / 24) * 2 * math.pi
    temp = 20 + 2.5 * math.sin(a - 9 / 24 * 2 * math.pi)
    hum = 55 + 12 * math.sin(a - 3 / 24 * 2 * math.pi)
    if 7 <= hour < 7.5:              # a hot shower
        hum += 20
    day.append((minute, temp + random.gauss(0, 0.2),
                hum + random.gauss(0, 1)))

temps = [t for _, t, _ in day]
hums = [h for _, _, h in day]
humid_minutes = 10 * sum(1 for h in hums if h > 65)
print(f"temperature: min {min(temps):.1f}, "
      f"max {max(temps):.1f}, avg {mean(temps):.1f} °C")
print(f"humidity   : min {min(hums):.0f}, "
      f"max {max(hums):.0f}, avg {mean(hums):.0f} %")
print(f"above 65 % humidity: {humid_minutes / 60:.1f} h")
