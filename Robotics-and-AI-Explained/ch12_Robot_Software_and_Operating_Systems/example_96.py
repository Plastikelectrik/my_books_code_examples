# Topics, publishers and subscribers in pure Python
from collections import defaultdict

class Bus:
    def __init__(self):
        self.subs = defaultdict(list)

    def subscribe(self, topic, callback):
        self.subs[topic].append(callback)

    def publish(self, topic, msg):
        for callback in self.subs[topic]:
            callback(msg)

bus = Bus()

def safety_monitor(scan):
    if min(scan) < 0.3:
        bus.publish("/cmd", {"speed": 0.0})
        print("safety: obstacle at", min(scan),
              "m -> stop")

def logger(msg):
    print("log: speed command", msg["speed"])

bus.subscribe("/scan", safety_monitor)
bus.subscribe("/cmd", logger)

bus.publish("/cmd", {"speed": 0.5})
bus.publish("/scan", [1.2, 0.9, 1.5])
bus.publish("/scan", [1.0, 0.25, 0.8])
