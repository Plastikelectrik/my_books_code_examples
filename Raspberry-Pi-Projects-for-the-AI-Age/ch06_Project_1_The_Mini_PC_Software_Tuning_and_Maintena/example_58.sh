sudo apt install cups
sudo usermod -aG lpadmin $USER
lpstat -e        # list detected printers
