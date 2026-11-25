docker run --rm -it --network none \
  -v /srv/cleanroom/kettle/spec:/spec:ro \
  -v /srv/cleanroom/kettle/rebuild:/work \
  -w /work python:3.13-slim bash
