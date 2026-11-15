# Remove missing values and outliers from readings
import csv, io
import numpy as np

raw = """time,distance_cm
0,52.1
1,51.8
2,
3,49.9
4,999
5,48.7
6,47.9
7,-5
8,46.8
"""
rows = list(csv.DictReader(io.StringIO(raw)))
values = []
for r in rows:
    text = r["distance_cm"].strip()
    if text == "":
        continue                  # missing value
    d = float(text)
    if 2 <= d <= 400:             # sensor valid range
        values.append(d)
print("raw rows:", len(rows))
print("clean values:", values)
print("mean:", round(np.mean(values), 2), "cm")
