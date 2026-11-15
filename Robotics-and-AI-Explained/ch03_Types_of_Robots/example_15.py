# Store robot types and filter them by property
robots = [
    {"name": "industrial arm", "moves": "fixed",
     "where": "factory", "payload_kg": 20},
    {"name": "cobot", "moves": "fixed",
     "where": "factory", "payload_kg": 10},
    {"name": "AMR", "moves": "wheels",
     "where": "warehouse", "payload_kg": 600},
    {"name": "robot vacuum", "moves": "wheels",
     "where": "home", "payload_kg": 0.5},
    {"name": "quadruped", "moves": "legs",
     "where": "outdoor", "payload_kg": 14},
    {"name": "quadcopter", "moves": "propellers",
     "where": "air", "payload_kg": 2},
    {"name": "ROV", "moves": "thrusters",
     "where": "water", "payload_kg": 5},
]

mobile = [r["name"] for r in robots
          if r["moves"] != "fixed"]
print("mobile robots:")
for name in mobile:
    print("  -", name)

heavy = [r for r in robots if r["payload_kg"] >= 10]
for r in sorted(heavy, key=lambda r: -r["payload_kg"]):
    print(f"{r['name']:15s} carries {r['payload_kg']} kg")
