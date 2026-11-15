# Remove a spike from distance readings
import statistics

readings = [50, 51, 49, 50, 180, 50, 49, 51, 50, 48]
window = 3
avg, med = [], []
for i in range(len(readings) - window + 1):
    part = readings[i:i + window]
    avg.append(round(sum(part) / window, 1))
    med.append(statistics.median(part))
print("raw   :", readings)
print("average:", avg)
print("median :", med)
