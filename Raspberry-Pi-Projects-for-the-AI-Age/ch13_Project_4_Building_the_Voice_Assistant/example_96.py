from gpiozero import LED, Button
from openwakeword.model import Model
from audio import find_device, frames
from stt import transcribe
from intents import parse, handle
from tts import say
from skills import start_timer, add_note
from record import record_command
import intents

led, mute_button = LED(17), Button(27)
muted = False

def toggle_mute():
    global muted
    muted = not muted
    led.on() if muted else led.off()
mute_button.when_pressed = toggle_mute

wake = Model(wakeword_models=["hey_jarvis"],
             inference_framework="onnx")
mic = find_device("usb")
spk = find_device("usb", "output")
stream = frames(mic)

def respond(text):
    intent, slots = parse(text)
    if intent == "set_timer":
        n = intents.to_number(slots[0])
        if n:
            start_timer(n * intents.UNITS[slots[1]],
                        lambda t: say(t, spk))
    elif intent == "add_note":
        add_note(slots[0])
    return handle(intent, slots)

for frame in stream:                      # IDLE
    if muted or wake.predict(frame)["hey_jarvis"] < 0.5:
        continue
    wake.reset()
    led.blink(0.1, 0.1)                   # LISTENING
    audio = record_command(stream)
    led.blink(0.05, 0.05)                 # THINKING
    text = transcribe(audio)
    answer = respond(text) if text else "Sorry?"
    led.on()                              # SPEAKING
    say(answer, spk)
    led.off()                             # back to IDLE
