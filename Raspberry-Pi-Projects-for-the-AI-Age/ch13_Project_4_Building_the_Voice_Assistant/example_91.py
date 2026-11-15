import re, datetime

WORDS = {"zero": 0, "one": 1, "two": 2, "three": 3,
         "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
         "twelve": 12, "fifteen": 15, "twenty": 20,
         "thirty": 30, "forty": 40, "fifty": 50,
         "a": 1, "an": 1}

def to_number(text):
    """'25', 'twenty five' or 'a' -> int, else None."""
    text = text.strip().lower()
    if text.isdigit():
        return int(text)
    parts = text.replace("-", " ").split()
    if parts and all(p in WORDS for p in parts):
        return sum(WORDS[p] for p in parts)
    return None

UNITS = {"second": 1, "minute": 60, "hour": 3600}
NUM = r"([\w\- ]+?)"
OPS = r"(plus|minus|times)"
PATTERNS = [
    ("set_timer",
     rf"timer for {NUM} (second|minute|hour)s?"),
    ("get_time", r"what time is it|tell me the time"),
    ("add_note", r"(?:note|remember)[:,]? (.+)"),
    ("calculate", rf"what is {NUM} {OPS} {NUM}$"),
    ("media",
     r"(pause|play|stop) the (film|movie|music)"),
]

def parse(text):
    t = text.lower().strip(" .?!")
    for intent, pattern in PATTERNS:
        m = re.search(pattern, t)
        if m:
            return intent, m.groups()
    return "unknown", (t,)

def handle(intent, slots, now=None):
    now = now or datetime.datetime.now()
    if intent == "set_timer":
        n = to_number(slots[0])
        if n is None:
            return "Sorry, I did not get the number."
        secs = n * UNITS[slots[1]]
        return f"Timer: {n} {slots[1]}s ({secs} s)."
    if intent == "get_time":
        return f"It is {now:%H:%M}."
    if intent == "add_note":
        return f"I noted: {slots[0]}."
    if intent == "calculate":
        a, op, b = slots
        a, b = to_number(a), to_number(b)
        if a is None or b is None:
            return "Sorry, I can only use whole numbers."
        result = {"plus": a + b, "minus": a - b,
                  "times": a * b}[op]
        return f"{a} {op} {b} is {result}."
    if intent == "media":
        return f"OK, {slots[0]} the {slots[1]}."
    return "Let me think about that."   # LLM fallback

if __name__ == "__main__":
    demo_time = datetime.datetime(2026, 1, 1, 14, 5)
    tests = ["Set a timer for twenty five minutes.",
             "Set a timer for 90 seconds",
             "What time is it?",
             "Note: buy milk and bread",
             "What is twelve times eight",
             "Pause the film",
             "Why is the sky blue?"]
    for s in tests:
        intent, slots = parse(s)
        answer = handle(intent, slots, demo_time)
        print(f"{intent:9s} | {answer}")
