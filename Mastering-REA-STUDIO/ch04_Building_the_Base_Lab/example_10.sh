cd ~/studio/targets/kettle
mkdir -p bin
gcc -O1 -g -Wall -o bin/kettle src/kettle.c
cp bin/kettle bin/kettle-stripped
strip bin/kettle-stripped
./bin/kettle green; ./bin/kettle black 5
