TOOLS_PROMPT = """Choose exactly one tool and reply with
JSON only, like {"tool": "...", "args": {...}}.
Tools:
- set_timer: args {"seconds": integer}
- media: args {"action": "play" | "pause" | "stop"}
- lamp: args {"on": true | false}
- answer: args {"text": "short spoken answer"}
Use "answer" for questions and small talk."""
