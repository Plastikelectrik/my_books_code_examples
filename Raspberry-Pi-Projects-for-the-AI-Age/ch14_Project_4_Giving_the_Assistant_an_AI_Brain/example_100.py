import json, urllib.request

URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:1.5b"

def chat(messages, json_mode=False, timeout=60):
    body = {"model": MODEL, "messages": messages,
            "stream": False,
            "options": {"temperature": 0.2}}
    if json_mode:
        body["format"] = "json"
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req,
                                timeout=timeout) as r:
        return json.load(r)["message"]["content"]

if __name__ == "__main__":
    print(chat([{"role": "user",
                 "content": "Name three planets."}]))
