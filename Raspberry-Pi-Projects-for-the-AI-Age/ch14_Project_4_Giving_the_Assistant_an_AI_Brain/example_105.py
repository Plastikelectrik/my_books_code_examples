import re

def sentences(stream):
    """Join streamed text pieces into whole sentences."""
    buf = ""
    for piece in stream:
        buf += piece
        while (m := re.search(r"[.!?](\s|$)", buf)):
            yield buf[:m.end()].strip()
            buf = buf[m.end():]
    if buf.strip():
        yield buf.strip()

pieces = ["Air scatters ", "blue light ", "more. So the ",
          "sky looks blue. At sunset", " it turns red."]
for s in sentences(pieces):
    print("SPEAK:", s)
