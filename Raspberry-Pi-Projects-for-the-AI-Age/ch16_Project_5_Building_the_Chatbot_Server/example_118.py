import hmac

PASSWORD = os.environ.get("CHATBOT_PASSWORD", "")

@app.before_request
def check_password():
    auth = request.authorization
    ok = auth and hmac.compare_digest(
        auth.password or "", PASSWORD)
    if not PASSWORD or not ok:
        return Response("Login required", 401,
            {"WWW-Authenticate": 'Basic realm="chatbot"'})
