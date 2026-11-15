TRANSITIONS = {
    ("IDLE", "order"): "DRIVING",
    ("DRIVING", "arrived"): "DELIVERING",
    ("DELIVERING", "done"): "IDLE",
}
state = "IDLE"
for event in ["order", "arrived", "oops", "done"]:
    state = TRANSITIONS.get((state, event), state)
    print(f"{event:8s} -> {state}")
