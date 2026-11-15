# Weighted match between a skill profile and roles
me = {"python": 3, "math": 2, "electronics": 4,
      "machine learning": 1, "mechanics": 4,
      "communication": 4, "safety": 2}
roles = {
    "robot technician": {"electronics": 3, "mechanics": 3,
                         "communication": 2},
    "ML engineer": {"python": 3, "math": 3,
                    "machine learning": 3},
    "integration eng.": {"electronics": 2, "mechanics": 2,
                         "python": 2, "safety": 2},
    "safety engineer": {"safety": 3, "mechanics": 2,
                        "electronics": 2},
}
scores = {}
for name, weights in roles.items():
    got = sum(min(me.get(s, 0), 5) * w
              for s, w in weights.items())
    best = sum(5 * w for w in weights.values())
    scores[name] = got / best
ranked = sorted(scores.items(), key=lambda x: -x[1])
for name, s in ranked:
    print(f"{name:17s} match {s:.0%}")
