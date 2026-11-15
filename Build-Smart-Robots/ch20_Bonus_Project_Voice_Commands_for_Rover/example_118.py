# Runs on Rover with a USB microphone and a Vosk model
import json
import queue
import time
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from rover import Rover
from voice_parser import CommandParser
from voice_executor import Executor

L = 0.154
PHRASES = ["rover forward", "rover back", "rover left",
           "rover right", "rover stop", "rover faster",
           "rover slower", "[unk]"]
audio = queue.Queue()
bot = Rover()
parser = CommandParser()
ex = Executor(lambda v, w: bot.velocity(v - w * L / 2,
                                        v + w * L / 2))
rec = KaldiRecognizer(Model("model"), 16000,
                      json.dumps(PHRASES))

def cb(indata, frames, t, status):
    audio.put(bytes(indata))

try:
    with sd.RawInputStream(samplerate=16000,
                           blocksize=1600, dtype="int16",
                           channels=1, callback=cb):
        while True:
            now = time.monotonic()
            while not audio.empty():
                if rec.AcceptWaveform(audio.get()):
                    res = json.loads(rec.Result())
                    text = res["text"]
                    if text:
                        cmd = parser.parse(text)
                        print(text, "->", cmd)
                        ex.handle(cmd, now)
            ex.tick(now)
            time.sleep(0.1)
finally:
    bot.close()
