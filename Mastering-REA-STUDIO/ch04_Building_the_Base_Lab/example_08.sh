sdkmanager "platform-tools" "emulator" \
  "system-images;android-35;google_apis;x86_64"
avdmanager create avd -n studio35 \
  -k "system-images;android-35;google_apis;x86_64"
emulator -avd studio35 -no-snapshot-save &
adb wait-for-device && adb devices
