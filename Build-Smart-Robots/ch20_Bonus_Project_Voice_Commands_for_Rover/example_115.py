# Runs on a computer with a microphone and a Vosk model
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

PHRASES = ["rover forward", "rover back", "rover left",
           "rover right", "rover stop", "rover faster",
           "rover slower", "rover come home", "[unk]"]
RATE = 16000
audio = queue.Queue()

def callback(indata, frames, time_info, status):
    audio.put(bytes(indata))

model = Model("model")
rec = KaldiRecognizer(model, RATE, json.dumps(PHRASES))
with sd.RawInputStream(samplerate=RATE, blocksize=8000,
                       dtype="int16", channels=1,
                       callback=callback):
    print("Listening... say 'rover stop' to end")
    while True:
        if rec.AcceptWaveform(audio.get()):
            text = json.loads(rec.Result())["text"]
            if text:
                print("heard:", text)
            if text == "rover stop":
                break
