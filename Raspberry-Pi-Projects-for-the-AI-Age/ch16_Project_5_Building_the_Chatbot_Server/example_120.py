TESTS = [
    ("How do I restart the router?",
     ["reset", "two seconds"]),
    ("When is the boiler serviced?", ["september"]),
    ("What is the Wi-Fi password?", ["label"]),
]
answers = [   # example answers from a test run
    "Hold the reset button for two seconds [1].",
    "The boiler service is every September [1].",
    "I do not know the password.",
]

def score(answer, must):
    a = answer.lower()
    hits = sum(1 for m in must if m in a)
    return hits / len(must)

total = 0
for (q, must), a in zip(TESTS, answers):
    s = score(a, must)
    total += s
    mark = "PASS" if s == 1 else "FAIL"
    print(f"{mark} {s:4.0%}  {q}")
print(f"overall: {total / len(TESTS):.0%}")
