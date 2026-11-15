import math, re
from collections import Counter

DOCS = {
 "router.txt": "The router admin page is at 192.168.1.1. "
   "The Wi-Fi password is on a label under the router. "
   "Restart the router by holding the reset button "
   "for two seconds only.",
 "heating.txt": "The heating runs from 6:00 to 22:00. "
   "In summer the heating is off. The boiler service "
   "is every September.",
 "media.txt": "Films are on the NAS in the Movies "
   "folder. The media center updates its library "
   "at startup.",
}

def chunks(text, max_words=12):
    """Group sentences into chunks of up to max_words."""
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    cur = []
    for s in sents:
        if cur and len(" ".join(cur + [s]).split()) \
                > max_words:
            yield " ".join(cur)
            cur = []
        cur.append(s)
    if cur:
        yield " ".join(cur)

def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())

index = [(name, c) for name, t in DOCS.items()
         for c in chunks(t)]
df = Counter(w for _, c in index for w in set(tokens(c)))
N = len(index)

def vector(text):
    tf = Counter(tokens(text))
    return {w: n * math.log((N + 1) / (df.get(w, 0) + 1))
            for w, n in tf.items()}

def cosine(a, b):
    dot = sum(a[w] * b.get(w, 0) for w in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

vecs = [vector(c) for _, c in index]
print(f"{len(DOCS)} documents -> {N} chunks")
for q in ["How do I restart the router?",
          "When is the boiler serviced?"]:
    qv = vector(q)
    scores = [cosine(qv, v) for v in vecs]
    best = max(range(N), key=scores.__getitem__)
    print(f"Q: {q}")
    print(f"   {index[best][0]} ({scores[best]:.2f})")
    print(f"   '{index[best][1][:44]}...'")
