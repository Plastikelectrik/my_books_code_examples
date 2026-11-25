import sys
import r2pipe

path, *consts = sys.argv[1:]
wanted = {c.lower() for c in consts}
r2 = r2pipe.open(path, flags=["-2"])
r2.cmd("aaa")
for fn in r2.cmdj("aflj") or []:
    addr = fn.get("addr", fn.get("offset"))
    ops = r2.cmdj(f"pdfj @ {addr}") or {}
    text = " ".join(o.get("disasm", "")
                    for o in ops.get("ops", []))
    found = {c for c in wanted if c in text}
    if found == wanted:
        print(hex(addr), fn["name"], fn["size"])
r2.quit()
