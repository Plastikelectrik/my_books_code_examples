import csv
import sys

src, base_from, base_to = sys.argv[1:4]
delta = int(base_to, 16) - int(base_from, 16)
with open(src, newline="") as f:
    for row in csv.DictReader(f):
        addr = int(row["address"], 16) + delta
        name = row["name"].strip()
        print(f"afn {name} {addr:#x}")
