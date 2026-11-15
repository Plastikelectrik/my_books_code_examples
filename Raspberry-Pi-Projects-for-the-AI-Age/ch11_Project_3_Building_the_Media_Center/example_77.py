import re

MOVIE = re.compile(r"^(?P<title>.+) \((?P<year>\d{4})\)"
                   r"\.(mkv|mp4|m4v|webm)$")
EPISODE = re.compile(r"S(?P<s>\d{2})E(?P<e>\d{2})", re.I)

def check_movie(folder, filename):
    if not MOVIE.match(filename):
        return "rename to 'Title (Year).mkv'"
    if folder != filename.rsplit(".", 1)[0]:
        return "folder name should match the file"
    return "ok"

def suggest_episode(show, filename):
    m = EPISODE.search(filename)
    if not m:
        return "no SxxEyy found"
    s, e = int(m["s"]), int(m["e"])
    ext = filename.rsplit(".", 1)[1]
    return f"Season {s:02d}/{show} S{s:02d}E{e:02d}.{ext}"

films = [("Big Buck Bunny (2008)",
          "Big Buck Bunny (2008).mkv"),
         ("Sintel", "sintel.mkv"),
         ("Tears of Steel (2012)",
          "Tears of Steel (2012).mp4")]
for folder, name in films:
    print(f"{name:27s} {check_movie(folder, name)}")
for raw in ["my.series.s01e03.1080p.mkv",
            "episode 4.mkv"]:
    tip = suggest_episode("My Series", raw)
    print(f"{raw:27s} {tip}")
