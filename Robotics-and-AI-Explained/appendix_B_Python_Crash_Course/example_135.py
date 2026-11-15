for i in range(3):
    print("for loop, step", i)

battery = 100
trips = 0
while battery > 30:
    battery -= 25     # battery = battery - 25
    trips += 1
print(f"trips: {trips}, battery left: {battery}")

for reading in [80, 60, 15, 90]:
    if reading < 20:
        print("obstacle! stopping the scan")
        break
    print("reading ok:", reading)
