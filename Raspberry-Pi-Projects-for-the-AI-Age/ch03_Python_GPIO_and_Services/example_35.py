import logging, sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("monitor")

for temp in [52.0, 71.5, 83.2]:
    if temp > 80:
        log.error("CPU %.1f °C: throttling likely", temp)
    elif temp > 70:
        log.warning("CPU at %.1f °C: check cooling", temp)
    else:
        log.info("CPU at %.1f °C", temp)
log.debug("not shown, because the level is INFO")
