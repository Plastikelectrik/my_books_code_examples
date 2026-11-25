mitmdump -nr ~/studio/captures/run2.mitm \
  --set hardump=$HOME/studio/captures/run2.har
rea inspect-web-network-capture \
  ~/studio/captures/run2.har har
