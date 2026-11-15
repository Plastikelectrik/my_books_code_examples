# Run in the same folder as dashboard.py
import os
os.environ["ROVER_TOKEN"] = "test-token"
from dashboard import app

client = app.test_client()
r = client.post("/api/drive", json={"v": 0.2, "w": 0})
print("without token:", r.status_code)
r = client.post("/api/drive", json={"v": 5, "w": -9},
                headers={"X-Token": "test-token"})
print("with token:", r.status_code, r.get_json())
st = client.get("/api/status").get_json()
print("status: v =", st["v"], "w =", st["w"])
