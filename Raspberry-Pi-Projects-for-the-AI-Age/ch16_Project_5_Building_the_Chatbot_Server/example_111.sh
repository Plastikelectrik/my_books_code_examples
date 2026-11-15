mkdir -p ~/chatbot/docs ~/chatbot/static
cd ~/chatbot
python3 -m venv .venv
source .venv/bin/activate
pip install flask gunicorn numpy faster-whisper piper-tts
sudo apt install -y ffmpeg
