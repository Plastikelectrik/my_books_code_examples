gcc -O1 -o kettle_enc kettle_enc.c
./kettle_enc
strings -n 4 kettle_enc | grep -c green
