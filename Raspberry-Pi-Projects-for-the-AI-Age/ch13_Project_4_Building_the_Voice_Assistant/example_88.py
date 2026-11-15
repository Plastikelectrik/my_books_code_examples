from openwakeword.model import Model
from audio import find_device, frames

model = Model(wakeword_models=["hey_jarvis"],
              inference_framework="onnx")
mic = find_device("usb")
print("Say 'hey Jarvis' ... (Ctrl+C to stop)")
for frame in frames(mic):
    scores = model.predict(frame)
    score = scores["hey_jarvis"]
    if score > 0.5:
        print(f"Wake word! score={score:.2f}")
        model.reset()          # avoid double triggers
