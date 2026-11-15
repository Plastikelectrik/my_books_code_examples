import datetime, pathlib, sys

LOG = pathlib.Path("build_log.md")

def add(note):
    now = datetime.datetime.now()
    stamp = now.strftime("%Y-%m-%d %H:%M")
    with LOG.open("a") as f:
        f.write(f"- {stamp}  {note}\n")

notes = sys.argv[1:] or ["Installed Batocera",
                         "Paired two gamepads"]
for n in notes:
    add(n)
print(LOG.read_text().strip())
