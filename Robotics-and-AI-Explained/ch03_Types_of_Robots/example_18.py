# Energy per kg per meter for different robots
robots = {                # (power W, mass kg, speed m/s)
    "wheeled AMR": (40, 50, 1.0),
    "quadruped": (300, 30, 1.5),
    "humanoid": (500, 60, 1.0),
    "quadcopter": (200, 1.5, 10.0),
}
g = 9.81
print("robot         cost of transport (lower=better)")
for name, (p, m, v) in robots.items():
    cot = p / (m * g * v)     # dimensionless number
    print(f"{name:13s} {cot:6.2f}")
