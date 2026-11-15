from faster_whisper import WhisperModel
from piper import PiperVoice

stt_model = WhisperModel("base", device="cpu",
                         compute_type="int8")
VOICE_FILE = BASE / "en_US-lessac-medium.onnx"
voice = PiperVoice.load(str(VOICE_FILE))

@app.post("/api/stt")
def stt():
    audio = request.files["audio"]
    with tempfile.NamedTemporaryFile(suffix=".webm") as f:
        audio.save(f.name)
        segments, _ = stt_model.transcribe(
            f.name, beam_size=1, vad_filter=True)
        text = " ".join(s.text for s in segments)
    return {"text": text.strip()}

@app.post("/api/tts")
def tts():
    text = request.json["text"][:1000]  # limit length
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wav:
        voice.synthesize_wav(text, wav)
    buf.seek(0)
    return send_file(buf, mimetype="audio/wav")
