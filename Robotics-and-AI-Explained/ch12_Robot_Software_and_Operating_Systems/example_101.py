# Use Python's logging module with time and level
import logging, io

stream = io.StringIO()
logging.basicConfig(stream=stream, level=logging.INFO,
                    format="%(levelname)s %(name)s: "
                           "%(message)s")
log = logging.getLogger("planner")

log.info("new goal received: kitchen")
log.warning("path blocked, replanning")
log.debug("this detail is hidden at INFO level")
log.error("no path found after 3 tries")
print(stream.getvalue().strip())
