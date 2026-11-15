readings = [120, 95, 80, 40, 22]
print("first:", readings[0])
print("last:", readings[-1])
print("middle three:", readings[1:4])
readings.append(18)
print("after append:", readings)
print("count:", len(readings))
print("min, max:", min(readings), max(readings))
print("sorted:", sorted(readings))
