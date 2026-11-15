import paho.mqtt.publish as publish

def lamp(on):
    publish.single("cmnd/desk_lamp/POWER",
                   "ON" if on else "OFF",
                   hostname="localhost")
