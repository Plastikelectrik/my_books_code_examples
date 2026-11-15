sudo apt update && sudo apt full-upgrade -y
sudo apt install -y python3-venv python3-opencv git
python3 -m venv --system-site-packages ~/rover-env
source ~/rover-env/bin/activate
pip install pyserial scikit-learn flask joblib
sudo usermod -aG dialout $USER   # serial port access
