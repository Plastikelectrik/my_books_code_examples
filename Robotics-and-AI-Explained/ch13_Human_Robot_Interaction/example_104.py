# Fuzzy matching tolerates small recognition errors
import difflib

INTENTS = {"go to the kitchen": ("goto", "kitchen"),
           "go to the charging station": ("goto", "dock"),
           "bring me water": ("fetch", "water"),
           "stop": ("stop", None)}

def understand(text):
    best = difflib.get_close_matches(
        text.lower(), INTENTS.keys(), n=1, cutoff=0.0)[0]
    score = difflib.SequenceMatcher(
        None, text.lower(), best).ratio()
    if score >= 0.8:
        return INTENTS[best], "execute"
    if score >= 0.5:
        question = f"ask: did you mean '{best}'?"
        return INTENTS[best], question
    return None, "say: sorry, I did not understand"

for heard in ["go to the kitchen", "go to the kitchn",
              "bring me watter", "go to charging",
              "play some music"]:
    intent, action = understand(heard)
    print(f"'{heard}' -> {intent}")
    print("    ", action)
