cm = [120, 95, 80, 40, 22]
meters = [d / 100 for d in cm]
close = [d for d in cm if d < 50]
print("meters:", meters)
print("close:", close)
