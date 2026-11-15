from faster_whisper import WhisperModel

model = WhisperModel("base.en", device="cpu",
                     compute_type="int8")

def transcribe(audio):
    """audio: float32 numpy array at 16 kHz."""
    segments, info = model.transcribe(
        audio, language="en", beam_size=1,
        vad_filter=True)
    return " ".join(s.text for s in segments).strip()
