unxz frida-server-*-android-x86_64.xz
mv frida-server-*-android-x86_64 frida-server
adb root
adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell "/data/local/tmp/frida-server &"
frida-ps -U | head
