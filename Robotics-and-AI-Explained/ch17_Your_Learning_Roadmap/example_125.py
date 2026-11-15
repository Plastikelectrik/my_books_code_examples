# Split weekly hours by priority, in 30-minute blocks
hours_per_week = 6
priorities = {"Python practice": 3, "math review": 1,
              "robot project": 4, "reading / videos": 2}

blocks = int(hours_per_week * 2)           # 30-min blocks
total = sum(priorities.values())
plan = {k: int(blocks * v / total) for k, v in
        priorities.items()}
left = blocks - sum(plan.values())
for k in sorted(priorities, key=priorities.get,
                reverse=True)[:left]:
    plan[k] += 1                           # use leftovers
for k, b in plan.items():
    print(f"{k:17s} {b * 0.5:4.1f} h")
total_h = sum(plan.values()) * 0.5
print(f"total             {total_h:4.1f} h")
