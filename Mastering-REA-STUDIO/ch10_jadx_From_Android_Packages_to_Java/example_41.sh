A=~/studio/targets/kettle-android/app-release.apk
rea inspect-android-package "$A"
rea search-android-classes "$A" "TextView"
rea inspect-apk-signature "$A"
