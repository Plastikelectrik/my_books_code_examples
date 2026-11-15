NEEDS_GB = {"Raspberry Pi OS Lite": 0.3,
            "Pi-hole + Unbound": 0.2,
            "CrowdSec + WireGuard": 0.2,
            "Frigate (2 cameras, Hailo)": 1.0,
            "voice assistant (base.en)": 0.8,
            "Ollama + 1.5B model": 2.0,
            "chatbot web app + index": 0.5}

def plan(board_gb, services, reserve=0.25):
    used = sum(NEEDS_GB[s] for s in services)
    limit = board_gb * (1 - reserve)
    state = "fits" if used <= limit else "TOO MUCH"
    print(f"{board_gb:2d} GB board: {used:.1f} GB "
          f"of {limit:.1f} GB usable -> {state}")

all_services = list(NEEDS_GB)
plan(4, all_services)
plan(8, all_services)
plan(16, all_services)
