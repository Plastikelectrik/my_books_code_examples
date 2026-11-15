import json

ALLOWED = {"set_timer": {"seconds": int},
           "media": {"action": str},
           "lamp": {"on": bool},
           "answer": {"text": str}}
MEDIA_ACTIONS = {"play", "pause", "stop"}
MAX_TIMER = 4 * 3600

def validate(raw):
    """Check a JSON tool call from the language model."""
    try:
        call = json.loads(raw)
    except json.JSONDecodeError:
        return None, "not valid JSON"
    tool, args = call.get("tool"), call.get("args", {})
    if tool not in ALLOWED:
        return None, f"tool {tool!r} not allowed"
    for name, kind in ALLOWED[tool].items():
        if not isinstance(args.get(name), kind):
            return None, f"bad argument {name!r}"
    if tool == "set_timer":
        if not 0 < args["seconds"] <= MAX_TIMER:
            return None, "timer out of range"
    if tool == "media":
        if args["action"] not in MEDIA_ACTIONS:
            return None, "unknown media action"
    return (tool, args), "ok"

replies = [
    '{"tool": "set_timer", "args": {"seconds": 600}}',
    '{"tool": "answer", "args": {"text": "Rayleigh."}}',
    '{"tool": "shell", "args": {"cmd": "rm -rf /"}}',
    '{"tool": "set_timer", "args": {"seconds": 999999}}',
    'Sure! I set the timer.',
]
for r in replies:
    result, why = validate(r)
    print(f"{why:26s} {result[0] if result else '-'}")
