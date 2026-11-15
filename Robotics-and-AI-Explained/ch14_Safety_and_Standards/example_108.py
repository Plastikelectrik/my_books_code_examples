# Rank hazards by severity x probability
hazards = [
    ("pinch point at gripper", 3, 3),
    ("robot hits person at full speed", 4, 2),
    ("battery overheats", 4, 1),
    ("trip over charging cable", 2, 3),
    ("loud noise", 1, 2),
]

def level(score):
    if score >= 9: return "HIGH"     # must reduce
    if score >= 5: return "MEDIUM"   # reduce if possible
    return "LOW"                     # monitor

ranked = sorted(hazards, key=lambda h: -(h[1] * h[2]))
for name, sev, prob in ranked:
    score = sev * prob
    print(f"{score:2d} {name:32s} {level(score)}")
