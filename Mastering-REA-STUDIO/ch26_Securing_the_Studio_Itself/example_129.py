import json
import re
import sys

RISKY = [r"\bcurl\b", r"\bwget\b", r"\bssh\b",
         r"\bscp\b", r"\bnc\b", r"\brm\s+-rf\b",
         r"\bchmod\s+\+x\b", r"\bsudo\b"]

call = json.load(sys.stdin)
text = json.dumps(call.get("tool_input", {}))
for pattern in RISKY:
    if re.search(pattern, text):
        print(f"blocked by studio policy: {pattern}",
              file=sys.stderr)
        sys.exit(2)
sys.exit(0)
