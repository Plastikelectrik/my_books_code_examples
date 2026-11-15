import urllib.request

NTFY = "https://ntfy.sh/guardian-7f3k2q9x"  # secret topic
DRY_RUN = True

def notify(title, message, priority="default"):
    if DRY_RUN:
        print(f"[{priority}] {title}: {message}")
        return
    req = urllib.request.Request(NTFY,
        data=message.encode(), method="POST")
    req.add_header("Title", title)
    req.add_header("Priority", priority)
    urllib.request.urlopen(req, timeout=10)

notify("New device", "192.168.1.35 joined the network",
       "high")
notify("Pi-hole", "Blocked 20.4 % of queries today")
