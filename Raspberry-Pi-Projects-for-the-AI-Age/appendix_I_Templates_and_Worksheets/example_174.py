import logging, signal, sys, time, tomllib
from pathlib import Path

CONFIG = Path(__file__).with_name("settings.toml")
running = True

def load_config():
    with open(CONFIG, "rb") as f:
        return tomllib.load(f)

def stop(signum, frame):
    global running
    running = False                  # finish the loop

def do_work(cfg, log):
    log.info("working for %s", cfg["project"]["name"])

def main():
    cfg = load_config()
    logging.basicConfig(
        level=cfg["project"].get("log_level", "INFO"),
        format="%(levelname)s %(message)s",
        stream=sys.stdout)
    log = logging.getLogger("main")
    signal.signal(signal.SIGTERM, stop)   # systemd stop
    signal.signal(signal.SIGINT, stop)    # Ctrl+C
    while running:
        try:
            do_work(cfg, log)
        except Exception:
            log.exception("error; retrying in 10 s")
            time.sleep(10)
            continue
        time.sleep(60)
    log.info("stopped cleanly")

if __name__ == "__main__":
    main()
