# Ultrasonic distance and the effect of temperature
def speed_of_sound(temp_c):
    return 331.3 + 0.606 * temp_c       # m/s

echo_us = 2915                          # microseconds
for temp in [0, 20, 35]:
    v = speed_of_sound(temp)
    d = v * (echo_us / 1e6) / 2
    print(f"{temp:2d} C: speed {v:.1f} m/s -> "
          f"{d * 100:.1f} cm")
