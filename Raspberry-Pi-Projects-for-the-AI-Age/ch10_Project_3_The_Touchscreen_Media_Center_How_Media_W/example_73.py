def size_gb(mbit_per_s, minutes):
    return mbit_per_s * minutes * 60 / 8 / 1000

videos = [("1080p H.264 film", 8, 120),
          ("1080p HEVC film", 5, 120),
          ("4K HEVC film", 25, 120),
          ("4K HEVC, high quality", 60, 120)]
links = {"Wi-Fi (weak)": 20, "Wi-Fi (good)": 150,
         "Gigabit Ethernet": 940}

for name, rate, minutes in videos:
    print(f"{name:22s} {size_gb(rate, minutes):5.1f} GB")
print()
for link, speed in links.items():
    ok = [n for n, r, _ in videos if r * 1.5 <= speed]
    print(f"{link:17s} streams {len(ok)}/{len(videos)}")
