apktool b decoded-release -o lab-unsigned.apk
zipalign -p -f 4 lab-unsigned.apk lab-aligned.apk
keytool -genkeypair -keystore ~/lab-keys/lab.jks \
  -alias lab -keyalg RSA -keysize 3072 \
  -validity 365 -dname "CN=Kettle Lab"
apksigner sign --ks ~/lab-keys/lab.jks \
  --out lab-signed.apk lab-aligned.apk
apksigner verify --print-certs lab-signed.apk
