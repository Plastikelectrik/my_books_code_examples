E12 = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82]

def standard_above(r):
    decade = 1
    while True:
        for v in E12:
            if v * decade >= r:
                return v * decade
        decade *= 10

def led_resistor(supply_v, led_v, current_ma):
    r = (supply_v - led_v) / (current_ma / 1000)
    std = standard_above(r)
    real_ma = (supply_v - led_v) / std * 1000
    power_mw = (supply_v - led_v) * real_ma
    return r, std, real_ma, power_mw   # power in mW

cases = [("red LED on GPIO", 3.3, 2.0, 5),
         ("blue LED on GPIO", 3.3, 2.9, 3),
         ("white LED on 5 V", 5.0, 3.0, 10)]
for name, vs, vf, ma in cases:
    r, std, real, p = led_resistor(vs, vf, ma)
    print(f"{name:17s} {r:4.0f} ohm -> {std} ohm, "
          f"{real:.1f} mA")
