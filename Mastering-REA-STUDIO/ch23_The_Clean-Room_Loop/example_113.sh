sudo useradd --create-home builder
sudo mkdir -p /srv/cleanroom/kettle/spec
sudo mkdir -p /srv/cleanroom/kettle/rebuild
sudo cp ~/studio/specs/kettle/SPEC.md \
  /srv/cleanroom/kettle/spec/
sudo chown -R root:root /srv/cleanroom/kettle/spec
sudo chmod -R a+rX,go-w /srv/cleanroom/kettle/spec
sudo chown builder /srv/cleanroom/kettle/rebuild
chmod 700 ~
