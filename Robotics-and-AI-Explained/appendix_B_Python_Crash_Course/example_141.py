def parse_reading(text):
    try:
        value = float(text)
    except ValueError:
        print(f"  bad reading {text!r}, ignored")
        return None
    return value

for raw in ["12.5", "err", "40"]:
    print(raw, "->", parse_reading(raw))
