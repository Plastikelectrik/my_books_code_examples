# SUS: 10 answers from 1 to 5 -> score from 0 to 100
def sus(answers):
    total = 0
    for i, a in enumerate(answers, start=1):
        if i % 2 == 1:          # positive statements
            total += a - 1
        else:                   # negative statements
            total += 5 - a
    return total * 2.5

participants = {"nurse A": [5, 2, 4, 1, 4, 2, 5, 1, 4, 2],
                "nurse B": [4, 2, 4, 2, 3, 2, 4, 2, 4, 3],
                "porter":  [3, 4, 3, 3, 3, 3, 2, 4, 3, 4]}
scores = {p: sus(a) for p, a in participants.items()}
for p, s in scores.items():
    print(f"{p:8s}: SUS {s:5.1f}")
avg = sum(scores.values()) / len(scores)
print(f"average: {avg:.1f}")
