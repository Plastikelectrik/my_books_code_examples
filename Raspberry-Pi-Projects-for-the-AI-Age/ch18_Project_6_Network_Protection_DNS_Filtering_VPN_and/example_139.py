import json, urllib.request

BASE = "http://192.168.1.2/api"
PASSWORD = "your-pihole-password"
DRY_RUN = True
SAMPLE = {"queries": {"total": 48210, "blocked": 9842,
                      "percent_blocked": 20.41},
          "clients": {"active": 17}}

def request(path, method="GET", body=None, sid=None):
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(BASE + path, data=data,
                                 method=method)
    req.add_header("Content-Type", "application/json")
    if sid:
        req.add_header("X-FTL-SID", sid)
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.load(r) if r.length != 0 else {}

def summary():
    if DRY_RUN:
        return SAMPLE
    login = {"password": PASSWORD}
    auth = request("/auth", "POST", login)
    sid = auth["session"]["sid"]
    try:
        return request("/stats/summary", sid=sid)
    finally:
        request("/auth", "DELETE", sid=sid)   # log out

s = summary()
q = s["queries"]
print(f"queries today : {q['total']:,}")
print(f"blocked       : {q['blocked']:,} "
      f"({q['percent_blocked']:.1f} %)")
print(f"active clients: {s['clients']['active']}")
