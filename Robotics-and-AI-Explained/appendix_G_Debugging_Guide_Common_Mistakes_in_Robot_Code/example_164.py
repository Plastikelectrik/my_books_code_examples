readings = [120, -1, -1, 80, 0, 95]

bad = readings.copy()
for r in bad:
    if r <= 0:
        bad.remove(r)
print("buggy result :", bad)

good = [r for r in readings if r > 0]
print("correct result:", good)
