# Map internal state to a clear, consistent signal
def signal(state, turning=None, person_near=False):
    colors = {"idle": "green", "moving": "blue",
              "working": "yellow", "error": "red"}
    color = colors.get(state, "red")
    pattern = "steady"
    if state == "moving" and person_near:
        pattern = "slow pulse"
    if state == "error":
        pattern = "fast blink"
    side = f", {turning} turn light" if turning else ""
    return f"{color} {pattern}{side}"

print(signal("idle"))
print(signal("moving", turning="left"))
print(signal("moving", person_near=True))
print(signal("error"))
