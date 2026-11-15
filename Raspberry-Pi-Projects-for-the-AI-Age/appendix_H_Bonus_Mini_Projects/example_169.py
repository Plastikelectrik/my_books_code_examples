import datetime, html
from pathlib import Path

def build_page(notes, now):
    items = "\n".join(f"<li>{html.escape(n)}</li>"
                      for n in notes)
    items = items or "<li>Nothing to do!</li>"
    return f"""<!doctype html><html><head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="60">
<style>body{{font-family:sans-serif;background:#FDF2F8;
color:#3F0D1F;font-size:2em}} h1{{color:#BE185D}}</style>
</head><body>
<h1>{now:%A, %d %B}</h1><p>{now:%H:%M}</p>
<h2>To do</h2><ul>{items}</ul>
</body></html>"""

notes = ["Buy milk", "Water the plants", "Call <grandma>"]
now = datetime.datetime(2026, 11, 13, 8, 30)
page = build_page(notes, now)
Path("kiosk.html").write_text(page)
lines = page.splitlines()
print(lines[6])
print(lines[7])
print([l for l in lines if "grandma" in l][0])
