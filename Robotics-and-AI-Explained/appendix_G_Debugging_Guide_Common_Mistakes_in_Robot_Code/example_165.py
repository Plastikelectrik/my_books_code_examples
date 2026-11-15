def log_bad(msg, log=[]):
    log.append(msg)
    return log

def log_good(msg, log=None):
    if log is None:
        log = []
    log.append(msg)
    return log

print(log_bad("start"), log_bad("stop"))
print(log_good("start"), log_good("stop"))
