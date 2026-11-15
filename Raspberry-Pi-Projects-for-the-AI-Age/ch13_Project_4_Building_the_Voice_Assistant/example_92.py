import threading
from pathlib import Path

NOTES = Path.home() / "assistant" / "notes.txt"
timers = []

def start_timer(seconds, say):
    def ring():
        say("Your timer is finished.")
    t = threading.Timer(seconds, ring)
    t.daemon = True
    t.start()
    timers.append(t)

def add_note(text):
    NOTES.parent.mkdir(parents=True, exist_ok=True)
    with NOTES.open("a") as f:
        f.write(text.strip() + "\n")

def read_notes():
    if not NOTES.exists():
        return "You have no notes."
    lines = NOTES.read_text().splitlines()
    return "Your notes are: " + "; ".join(lines)
