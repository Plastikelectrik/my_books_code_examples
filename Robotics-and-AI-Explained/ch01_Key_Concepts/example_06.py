# On-off feedback control of room temperature
temp = 16.0      # current temperature in C
target = 21.0    # desired temperature
outside = 10.0

for minute in range(1, 41):
    heater_on = temp < target           # think
    if heater_on:                       # act
        temp += 0.9
    temp -= 0.05 * (temp - outside)     # heat loss
    if minute % 4 == 0:
        state = "ON" if heater_on else "OFF"
        print(f"min {minute:2d}: {temp:5.2f} C {state}")
