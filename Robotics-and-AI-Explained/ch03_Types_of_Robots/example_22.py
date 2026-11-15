# Score robot types against task requirements
types = {
    "wheeled":   {"flat": 3, "stairs": 0, "rough": 1,
                  "efficiency": 3, "air": 0},
    "legged":    {"flat": 2, "stairs": 3, "rough": 3,
                  "efficiency": 1, "air": 0},
    "tracked":   {"flat": 2, "stairs": 1, "rough": 3,
                  "efficiency": 2, "air": 0},
    "drone":     {"flat": 2, "stairs": 2, "rough": 2,
                  "efficiency": 0, "air": 3},
}

def best_for(needs):
    scores = {}
    for name, ability in types.items():
        scores[name] = sum(ability[k] * w
                           for k, w in needs.items())
    ranked = sorted(scores.items(), key=lambda s: -s[1])
    return ranked

warehouse = {"flat": 3, "efficiency": 2}
inspection = {"stairs": 2, "rough": 2, "flat": 1}
print("warehouse :", best_for(warehouse)[:2])
print("inspection:", best_for(inspection)[:2])
