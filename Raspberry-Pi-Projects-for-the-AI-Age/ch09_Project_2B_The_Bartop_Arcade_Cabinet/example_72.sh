python3 -m venv --system-site-packages ~/arcade/.venv
~/arcade/.venv/bin/pip install evdev
sudo modprobe uinput
echo uinput | sudo tee /etc/modules-load.d/uinput.conf
