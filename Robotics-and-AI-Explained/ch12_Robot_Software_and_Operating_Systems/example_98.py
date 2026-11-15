# States and transitions triggered by events
transitions = {
    ("IDLE", "order"): "GO_TO_PICKUP",
    ("GO_TO_PICKUP", "arrived"): "LOADING",
    ("LOADING", "loaded"): "DELIVERING",
    ("DELIVERING", "arrived"): "WAIT_CUSTOMER",
    ("WAIT_CUSTOMER", "taken"): "RETURN",
    ("RETURN", "arrived"): "IDLE",
}
low_battery_ok = {"IDLE", "RETURN"}

state = "IDLE"
events = ["order", "arrived", "loaded", "battery_low",
          "arrived", "taken", "arrived"]
for e in events:
    if e == "battery_low" and state not in low_battery_ok:
        print(f"{state:13s} + {e:11s} -> continue")
        continue
    new = transitions.get((state, e))
    if new is None:
        print(f"{state:13s} + {e:11s} -> ignored")
        continue
    print(f"{state:13s} + {e:11s} -> {new}")
    state = new
