sudo apt install -y meson ninja-build
tar xf rizin-src-*.tar.xz && cd rizin-*/
meson setup build
meson compile -C build
sudo meson install -C build
rizin -v
