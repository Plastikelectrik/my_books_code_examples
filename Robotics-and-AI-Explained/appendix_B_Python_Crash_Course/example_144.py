import csv

rows = [(0.0, 120), (0.1, 118), (0.2, 115)]
with open("log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time_s", "distance_cm"])
    writer.writerows(rows)

with open("log.csv") as f:
    for row in csv.DictReader(f):
        print(row["time_s"], row["distance_cm"])
