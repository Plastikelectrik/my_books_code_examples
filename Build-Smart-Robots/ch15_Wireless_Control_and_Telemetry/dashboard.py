# Runs on the Raspberry Pi: pip install flask
import os
import time
from flask import Flask, jsonify, request, abort

TOKEN = os.environ.get("ROVER_TOKEN", "change-me")
app = Flask(__name__)
state = {"dist": None, "batt": None, "v": 0.0,
         "w": 0.0, "updated": time.time()}

PAGE = """<!doctype html><html><body
style="font-family:sans-serif;max-width:420px">
<h2>Rover dashboard</h2>
<p>Distance: <b id="d">-</b> cm |
Battery: <b id="b">-</b> V</p>
<p><button onclick="go(0.15,0)">Forward</button>
<button onclick="go(0,1)">Left</button>
<button onclick="go(0,-1)">Right</button>
<button onclick="go(0,0)">STOP</button></p>
<script>
const tok = prompt("Token");
async function go(v, w) {
  await fetch("/api/drive", {method: "POST",
    headers: {"Content-Type": "application/json",
              "X-Token": tok},
    body: JSON.stringify({v: v, w: w})});
}
setInterval(async () => {
  const s = await (await fetch("/api/status")).json();
  document.getElementById("d").textContent = s.dist;
  document.getElementById("b").textContent = s.batt;
}, 500);
</script></body></html>"""

@app.get("/")
def page():
    return PAGE

@app.get("/api/status")
def status():
    return jsonify(state)

@app.post("/api/drive")
def drive():
    if request.headers.get("X-Token") != TOKEN:
        abort(403)
    cmd = request.get_json(force=True)
    v = max(-0.3, min(0.3, float(cmd.get("v", 0))))
    w = max(-1.5, min(1.5, float(cmd.get("w", 0))))
    state.update(v=v, w=w, updated=time.time())
    return jsonify(ok=True, v=v, w=w)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
