import csv
import sys

tables = []
for path in sys.argv[1:]:
    with open(path, newline="") as f:
        rows = {(r[0], r[1]): r[2] for r in csv.reader(f)}
    tables.append((path, rows))

base_path, base = tables[0]
for path, rows in tables[1:]:
    for key in sorted(set(base) | set(rows)):
        a, b = base.get(key), rows.get(key)
        if a != b:
            print(f"{key}: {base_path}={a} {path}={b}")
print("comparison finished")
