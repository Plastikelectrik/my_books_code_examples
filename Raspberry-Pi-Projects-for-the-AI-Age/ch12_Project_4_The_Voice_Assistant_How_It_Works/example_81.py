steps = {                   # seconds, example values
    "end of speech detection": 0.4,
    "speech-to-text (base.en)": 1.2,
    "intent (rules)": 0.01,
    "skill": 0.05,
    "text-to-speech (first audio)": 0.4,
}
total = sum(steps.values())
for name, sec in steps.items():
    share = sec / total * 100
    print(f"{name:30s} {sec:5.2f} s {share:4.0f} %")
print(f"{'total':30s} {total:5.2f} s")
