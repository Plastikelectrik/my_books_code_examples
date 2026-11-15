import numpy as np
from piper import PiperVoice
from audio import play

voice = PiperVoice.load(
    "/home/oscar/assistant/en_US-lessac-medium.onnx")

def say(text, device=None):
    audio = np.concatenate([
        chunk.audio_int16_array
        for chunk in voice.synthesize(text)])
    play(audio, voice.config.sample_rate, device)
