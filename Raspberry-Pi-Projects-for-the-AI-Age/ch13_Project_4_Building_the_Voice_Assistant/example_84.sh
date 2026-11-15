arecord -D plughw:2,0 -f S16_LE -r 16000 -c 1 \
        -d 5 test.wav
aplay -D plughw:3,0 test.wav
