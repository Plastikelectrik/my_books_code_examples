import json
from intents import parse, handle
from llm import chat
from validate import validate      # the validator above
from prompts import SYSTEM, TOOLS_PROMPT

def think(text, run_tool):
    intent, slots = parse(text)
    if intent != "unknown":
        return handle(intent, slots)
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "system", "content": TOOLS_PROMPT},
        {"role": "user", "content": text}]
    try:
        raw = chat(messages, json_mode=True)
    except OSError:
        return "Sorry, my brain is not available."
    result, why = validate(raw)
    if result is None:
        return "Sorry, I cannot do that."
    tool, args = result
    if tool == "answer":
        return args["text"]
    return run_tool(tool, args)
