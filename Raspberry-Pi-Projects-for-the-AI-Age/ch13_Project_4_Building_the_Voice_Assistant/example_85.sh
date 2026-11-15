mkdir -p ~/assistant && cd ~/assistant
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install sounddevice numpy openwakeword \
            faster-whisper piper-tts
