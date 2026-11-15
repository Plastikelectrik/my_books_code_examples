from difflib import SequenceMatcher

SKILLS = {"go": ["kitchen", "lab", "dock", "office"],
          "bring": ["water", "box", "tools"],
          "clean": ["floor", "table"]}
FORBIDDEN = ["stairs", "fast", "person", "fire"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def interpret(text):
    words = text.lower().replace(",", " ").split()
    for w in words:
        if w in FORBIDDEN:
            return "REFUSE", f"'{w}' is not allowed"
    best = (0.0, None, None)
    for skill, targets in SKILLS.items():
        for t in targets:
            s1 = max(similar(w, skill) for w in words)
            s2 = max(similar(w, t) for w in words)
            score = min(s1, s2)
            if score > best[0]:
                best = (score, skill, t)
    score, skill, target = best
    if score >= 0.85:
        return "EXECUTE", f"{skill} -> {target}"
    if score >= 0.6:
        return "CONFIRM", f"{skill} {target}?"
    return "REJECT", "unknown command"

for cmd in ["go to the kitchen", "bring me some watr",
            "clen the tabel", "go down the stairs",
            "dance for me", "bring tools to the lab"]:
    decision, info = interpret(cmd)
    print(f"{cmd:23s} {decision:8s} {info}")
