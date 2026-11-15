# Robot density 2024 (IFR World Robotics 2025)
import matplotlib.pyplot as plt

density = {"Korea": 1220, "Singapore": 818,
           "China": 567, "Germany": 449,
           "Japan": 446, "World avg.": 177}
for country, d in density.items():
    bar = "#" * (d // 50)
    print(f"{country:10s} {d:5d} {bar}")

plt.figure(figsize=(5, 2.8))
names = list(density)[::-1]
plt.barh(names, [density[n] for n in names])
plt.xlabel("robots per 10,000 manufacturing employees")
plt.title("Robot density, 2024")
plt.tight_layout()
plt.savefig("robot_density.png")
