cd ~/studio/targets/kettle
cp src/kettle.c src/kettle-1.1.c
mkdir -p bin-1.1
gcc -O1 -g -Wall -o bin-1.1/kettle src/kettle-1.1.c
cp bin-1.1/kettle bin-1.1/kettle-stripped
strip bin-1.1/kettle-stripped
