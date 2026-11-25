import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

RECIPES = [
    {"tea": "green", "temp": 80, "seconds": 130},
    {"tea": "black", "temp": 95, "seconds": 240},
    {"tea": "oolong", "temp": 90, "seconds": 180},
]
TOKEN = "lab-token-123"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/api/recipes":
            self.send_error(404)
            return
        if self.headers.get("X-Kettle-Token") != TOKEN:
            self.send_error(401)
            return
        body = json.dumps({"v": 2, "recipes": RECIPES})
        data = body.encode("utf-8")
        self.send_response(200)
        ctype = "application/json"
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


HTTPServer(("127.0.0.1", 8800), Handler).serve_forever()
