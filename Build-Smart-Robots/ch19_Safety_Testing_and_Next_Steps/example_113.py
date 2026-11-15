import logging
from logging.handlers import RotatingFileHandler

log = logging.getLogger("rover")
log.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(levelname)-7s %(message)s",
    datefmt="%H:%M:%S")

screen = logging.StreamHandler()
screen.setLevel(logging.INFO)          # less noise
screen.setFormatter(fmt)

file = RotatingFileHandler("rover.log",
                           maxBytes=1_000_000,
                           backupCount=5)
file.setLevel(logging.DEBUG)           # everything
file.setFormatter(fmt)

log.addHandler(screen)
log.addHandler(file)

log.info("mission started: kitchen -> office")
log.debug("pose x=0.41 y=0.12 th=0.30")
log.warning("obstacle at 28 cm, replanning")
log.error("no path to office, stopping")
print("lines in log file:",
      sum(1 for _ in open("rover.log")))
