import logging

from mitmproxy import http


class KettleAddon:
    def response(self, flow: http.HTTPFlow) -> None:
        req = flow.request
        if "X-Kettle-Token" in req.headers:
            req.headers["X-Kettle-Token"] = "REDACTED"
        if req.path.startswith("/api/recipes"):
            data = flow.response.json()
            n = len(data.get("recipes", []))
            v = data.get("v")
            logging.info("recipes=%d v=%s", n, v)


addons = [KettleAddon()]
