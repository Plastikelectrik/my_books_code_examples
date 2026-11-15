def estimate_tokens(text):
    return round(len(text.split()) / 0.75)

system = "You are a helpful assistant. " * 3
history = ["What is a black hole?",
           "A region where gravity is so strong that "
           "nothing, not even light, can escape.",
           "How are they formed?"]
document = "word " * 600          # a 600-word document

parts = {"system prompt": system,
         "history": " ".join(history),
         "document": document}
PREFILL, GENERATE = 60.0, 12.0    # tokens/s (examples)
total = 0
for name, text in parts.items():
    n = estimate_tokens(text)
    total += n
    print(f"{name:14s} {n:5d} tokens")
print(f"{'input total':14s} {total:5d} tokens")
wait = total / PREFILL
print(f"prefill ~{wait:.1f} s, then {GENERATE:.0f} tok/s")
