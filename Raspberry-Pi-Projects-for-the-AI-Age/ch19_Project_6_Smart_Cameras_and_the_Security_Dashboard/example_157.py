ORDER = {"OK": 0, "WARN": 1, "FAIL": 2}

def overall(results):
    worst = max(results, key=lambda r: ORDER[r[1]])
    return worst[1]

def check_disk(used_percent):
    if used_percent > 95:
        return "FAIL", f"disk {used_percent}% full"
    if used_percent > 85:
        return "WARN", f"disk {used_percent}% full"
    return "OK", f"disk {used_percent}%"

def check_service(name, active):
    if active:
        return "OK", "running"
    return "FAIL", "stopped"

results = [
    ("pihole-FTL", *check_service("pihole-FTL", True)),
    ("unbound", *check_service("unbound", True)),
    ("wg-quick@wg0", *check_service("wg", True)),
    ("crowdsec", *check_service("crowdsec", True)),
    ("frigate", *check_service("frigate", False)),
    ("recordings", *check_disk(88)),
]
for name, state, text in results:
    print(f"{state:4s}  {name:13s} {text}")
print("OVERALL:", overall(results))
