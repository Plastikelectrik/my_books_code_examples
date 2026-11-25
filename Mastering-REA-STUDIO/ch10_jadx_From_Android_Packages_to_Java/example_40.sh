cd ~/studio/targets/kettle-android
jadx -d out-debug app-debug.apk
ls out-debug
grep -rn "10007" out-debug/sources | head
