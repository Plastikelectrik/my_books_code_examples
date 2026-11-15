import json, re, urllib.request
from pathlib import Path

DOCS = Path.home() / "chatbot" / "docs"
INDEX = Path.home() / "chatbot" / "index.json"
EMBED_URL = "http://localhost:11434/api/embed"

def chunks(text, max_words=150):
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    cur = []
    for s in sents:
        if cur and len(" ".join(cur + [s]).split()) \
                > max_words:
            yield " ".join(cur)
            cur = cur[-1:]  # one sentence overlap
        cur.append(s)
    if cur:
        yield " ".join(cur)

def embed(texts):
    body = {"model": "nomic-embed-text", "input": texts}
    req = urllib.request.Request(
        EMBED_URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)["embeddings"]

items = []
for path in sorted(DOCS.glob("*.*")):
    if path.suffix not in (".txt", ".md"):
        continue
    parts = list(chunks(path.read_text()))
    for text, vec in zip(parts, embed(parts)):
        items.append({"source": path.name,
                      "text": text, "vector": vec})
    print(f"{path.name}: {len(parts)} chunks")
INDEX.write_text(json.dumps(items))
print(f"saved {len(items)} chunks to {INDEX}")
