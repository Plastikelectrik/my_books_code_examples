import json

COOLDOWN_S = 300
last_alert = {}

def should_alert(msg, now):
    ev = json.loads(msg)
    after = ev["after"]
    if ev["type"] != "new" or after["label"] != "person":
        return None
    if after["top_score"] < 0.75:
        return None
    if "front_door" not in after["current_zones"]:
        return None
    cam = after["camera"]
    last = last_alert.get(cam, -COOLDOWN_S)
    if now - last < COOLDOWN_S:
        return None
    last_alert[cam] = now
    return f"Person at the front door ({cam})"

def event(kind, label, score, zones, cam="entrance"):
    return json.dumps({"type": kind, "after": {
        "camera": cam, "label": label, "top_score": score,
        "current_zones": zones}})

samples = [
    (0, event("new", "person", 0.91, ["front_door"])),
    (30, event("update", "person", 0.93, ["front_door"])),
    (60, event("new", "cat", 0.88, ["front_door"])),
    (90, event("new", "person", 0.95, ["front_door"])),
    (400, event("new", "person", 0.62, ["front_door"])),
    (420, event("new", "person", 0.90, ["street"])),
    (500, event("new", "person", 0.88, ["front_door"])),
]
for t, msg in samples:
    print(f"t={t:3d}s -> {should_alert(msg, t) or '-'}")
