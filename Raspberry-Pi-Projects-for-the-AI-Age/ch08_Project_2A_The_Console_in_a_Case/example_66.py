import shutil, tempfile
from pathlib import Path
from xml.sax.saxutils import escape

SYSTEMS = {".nes": "nes", ".sfc": "snes", ".smc": "snes",
           ".gb": "gb", ".gbc": "gbc", ".gba": "gba",
           ".md": "megadrive", ".gen": "megadrive",
           ".sms": "mastersystem", ".a26": "atari2600"}

def sort_games(inbox, roms):
    moved = {}
    for f in sorted(Path(inbox).iterdir()):
        system = SYSTEMS.get(f.suffix.lower())
        if not system:
            print(f"skipped (unknown type): {f.name}")
            continue
        dest = Path(roms) / system
        dest.mkdir(parents=True, exist_ok=True)
        shutil.move(str(f), dest / f.name)
        moved.setdefault(system, []).append(f.name)
    return moved

def write_gamelist(folder, info):
    lines = ["<?xml version='1.0'?>", "<gameList>"]
    for fname, (name, author) in info.items():
        lines += ["  <game>",
                  f"    <path>./{escape(fname)}</path>",
                  f"    <name>{escape(name)}</name>",
                  f"    <developer>{escape(author)}"
                  "</developer>",
                  "  </game>"]
    lines.append("</gameList>")
    text = "\n".join(lines)
    (Path(folder) / "gamelist.xml").write_text(text)

# Demo with empty placeholder files in a temporary folder
base = Path(tempfile.mkdtemp())
inbox, roms = base / "inbox", base / "roms"
inbox.mkdir()
for n in ["space_rescue.nes", "tiny_quest.gb",
          "rally_demo.md", "readme.txt"]:
    (inbox / n).write_bytes(b"")
result = sort_games(inbox, roms)
for system, files in result.items():
    print(f"{system:10s} <- {', '.join(files)}")
meta = {"space_rescue.nes": ("Space Rescue", "A. Dev")}
write_gamelist(roms / "nes", meta)
print((roms / "nes" / "gamelist.xml").read_text())
