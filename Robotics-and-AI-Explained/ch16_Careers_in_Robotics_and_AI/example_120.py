# Compare your skill levels (0-5) with a role profile
me = {"python": 3, "math": 2, "electronics": 1,
      "machine learning": 2, "ros2": 0,
      "communication": 4, "linux": 2}
role = {"python": 4, "math": 3, "machine learning": 4,
        "ros2": 2, "linux": 3, "communication": 3}

print("skill             you  need  gap")
total_gap = 0
for skill, need in role.items():
    have = me.get(skill, 0)
    gap = max(0, need - have)
    total_gap += gap
    mark = "  <- learn" if gap >= 2 else ""
    print(f"{skill:17s} {have:3d} {need:5d} "
          f"{gap:4d}{mark}")
print("total gap:", total_gap, "points")
