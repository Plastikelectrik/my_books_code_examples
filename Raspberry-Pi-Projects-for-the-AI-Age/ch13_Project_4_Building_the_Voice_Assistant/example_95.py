TRANSITIONS = {
    ("IDLE", "wake"): "LISTENING",
    ("LISTENING", "speech_end"): "THINKING",
    ("LISTENING", "timeout"): "IDLE",
    ("THINKING", "answer_ready"): "SPEAKING",
    ("SPEAKING", "done"): "IDLE",
    ("IDLE", "mute"): "MUTED",
    ("MUTED", "mute"): "IDLE",
}
LED = {"IDLE": "off", "LISTENING": "on",
       "THINKING": "blink fast", "SPEAKING": "pulse",
       "MUTED": "red"}

def run(events, state="IDLE"):
    for ev in events:
        new = TRANSITIONS.get((state, ev), state)
        flag = "" if new != state else "  (ignored)"
        print(f"{ev:12s} {state:9s} -> {new:9s}"
              f" LED {LED[new]}{flag}")
        state = new
    return state

run(["wake", "speech_end", "answer_ready", "done",
     "mute", "wake", "mute", "wake", "timeout"])
