# Parse simple commands into safe, known actions
import re

SKILLS = {"go": ["kitchen", "office", "dock"],
          "pick": ["cup", "box", "book"],
          "place": ["table", "shelf"]}

def parse(command):
    plan = []
    for part in re.split(r",| then | and ", command):
        words = part.lower().split()
        verb = next((w for w in words
                     if w in SKILLS), None)
        if verb is None:
            continue
        target = next((w for w in words
                       if w in SKILLS[verb]), None)
        if target is None:
            return None, f"unknown target in '{part}'"
        plan.append((verb, target))
    return plan, "ok"

for cmd in ["go to the kitchen, pick the cup, "
            "place it on the table",
            "pick the cat and go to the dock"]:
    plan, status = parse(cmd)
    print("command:")
    print(" ", cmd)
    print("  status:", status)
    for verb, target in plan or []:
        print("  step:", verb, target)
