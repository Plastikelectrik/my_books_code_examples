adb uninstall com.example.kettle
adb install lab-signed.apk
adb shell am start -n \
  com.example.kettle/.MainActivity
