import base64, json, urllib.request

HOST, PORT = "mediacenter.local", 8080
USER, PASSWORD = "kodi", "change-me"
DRY_RUN = True                   # False = really send

def call(method, **params):
    body = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params:
        body["params"] = params
    data = json.dumps(body).encode()
    if DRY_RUN:                  # show what would be sent
        print("->", method)
        for key, value in params.items():
            print(f"     {key} = {value!r}")
        return None
    req = urllib.request.Request(
        f"http://{HOST}:{PORT}/jsonrpc", data=data,
        headers={"Content-Type": "application/json"})
    login = f"{USER}:{PASSWORD}".encode()
    token = base64.b64encode(login).decode()
    req.add_header("Authorization", "Basic " + token)
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.load(r).get("result")

call("JSONRPC.Ping")
call("GUI.ShowNotification", title="Dinner",
     message="Food is ready!", displaytime=8000)
call("Application.SetVolume", volume=40)
call("VideoLibrary.Scan")
