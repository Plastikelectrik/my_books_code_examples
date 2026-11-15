import io, json, os, tempfile, urllib.request, wave
from pathlib import Path
import numpy as np
from flask import Flask, Response, request, send_file
from retrieve import top_k

BASE = Path.home() / "chatbot"
CHAT_URL = "http://localhost:11434/api/chat"
EMBED_URL = "http://localhost:11434/api/embed"
MODEL = "qwen2.5:1.5b"
SYSTEM = ("You are a friendly home assistant. Answer "
          "clearly and briefly. When sources are given, "
          "use only them and cite them like [1]. If you "
          "do not know, say so.")

app = Flask(__name__, static_folder=str(BASE / "static"))
ITEMS = json.loads((BASE / "index.json").read_text())
MATRIX = np.array([it["vector"] for it in ITEMS])

def post(url, body):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=300)

def context_for(question):
    with post(EMBED_URL, {"model": "nomic-embed-text",
                          "input": [question]}) as r:
        qv = json.load(r)["embeddings"][0]
    hits = top_k(qv, MATRIX, k=3)
    return [ITEMS[i] for i, _ in hits]

@app.get("/")
def index():
    return app.send_static_file("index.html")

@app.post("/api/chat")
def chat():
    history = request.json["messages"][-8:]   # keep short
    question = history[-1]["content"]
    sources = context_for(question)
    system = SYSTEM
    if sources:
        listing = "\n".join(
            f"[{n}] ({s['source']}) {s['text']}"
            for n, s in enumerate(sources, 1))
        system += "\n\nSources:\n" + listing
    body = {"model": MODEL, "stream": True,
            "options": {"temperature": 0.3},
            "messages": [{"role": "system",
                          "content": system}] + history}

    def generate():
        with post(CHAT_URL, body) as r:
            for line in r:  # one JSON per line
                part = json.loads(line)
                yield part["message"]["content"]
        if sources:
            names = sorted({s["source"] for s in sources})
            yield "\n\nSources: " + ", ".join(names)
    return Response(generate(), mimetype="text/plain")
