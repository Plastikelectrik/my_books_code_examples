import tomllib
from pathlib import Path

Path("settings.toml").write_text("""
[assistant]
name = "Pixel"
wake_word = "hey_jarvis"
language = "en"

[audio]
sample_rate = 16000
volume = 0.8
""")

with open("settings.toml", "rb") as f:
    cfg = tomllib.load(f)

print("Assistant:", cfg["assistant"]["name"])
print("Wake word:", cfg["assistant"]["wake_word"])
print("Rate     :", cfg["audio"]["sample_rate"], "Hz")
