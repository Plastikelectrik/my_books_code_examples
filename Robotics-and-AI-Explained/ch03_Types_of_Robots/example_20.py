# Pressure increases about 1 bar every 10 m in water
RHO = 1025      # density of seawater, kg/m^3
g = 9.81
ATM = 101325    # pressure at the surface, pascals

for depth in [0, 10, 100, 1000, 4000]:
    p = ATM + RHO * g * depth
    print(f"{depth:5d} m: {p / 1e5:7.1f} bar")
