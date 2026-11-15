# Learn which word follows which, then generate text
import random
from collections import defaultdict

text = """the robot moves to the door . the robot opens
the door . the robot sees a box . the box is red .
the robot picks the box . the robot moves to the table
. the robot puts the box on the table ."""
words = text.split()

follows = defaultdict(list)
for a, b in zip(words, words[1:]):
    follows[a].append(b)

print("after 'robot':", sorted(set(follows["robot"])))
random.seed(3)
word, out = "the", ["the"]
for _ in range(15):
    word = random.choice(follows[word])
    out.append(word)
for i in range(0, len(out), 8):     # 8 words per line
    print(" ".join(out[i:i + 8]))
