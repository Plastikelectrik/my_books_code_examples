COLORS = {"OK": (0, 1, 0), "WARN": (1, 0.6, 0),
          "FAIL": (1, 0, 0), "VPN": (0, 0, 1)}

def light(overall, vpn_clients, night=False):
    """Choose the color and brightness of the LED."""
    if overall != "OK":
        color = COLORS[overall]
    elif vpn_clients:
        color = COLORS["VPN"]
    else:
        color = COLORS["OK"]
    level = 0.15 if night and overall == "OK" else 1.0
    return tuple(round(c * level, 2) for c in color)

cases = [("OK", 0, False), ("OK", 2, False),
         ("WARN", 0, False), ("FAIL", 1, True),
         ("OK", 0, True)]
for overall, vpn, night in cases:
    rgb = light(overall, vpn, night)
    tag = f"{overall:4s} vpn={vpn} night={night!s:5s}"
    print(tag, rgb)
