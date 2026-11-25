#include <stdio.h>
#include <string.h>

static int check(const char *c)
{
    if (strlen(c) != 8)
        return 0;
    unsigned h = 0;
    for (int i = 0; i < 8; i++) {
        if (c[i] < 'a' || c[i] > 'z')
            return 0;
        h = h * 31 + (unsigned char)c[i];
    }
    if (c[0] != 't' || c[7] != 'a')
        return 0;
    if ((c[1] ^ c[6]) != 0x13)
        return 0;
    if (c[2] + c[3] != 0xd7)
        return 0;
    if (c[5] - c[4] != 9)
        return 0;
    return h % 10007 == 1620;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        puts("usage: kettle-lock CODE");
        return 1;
    }
    puts(check(argv[1]) ? "OPEN" : "LOCKED");
    return 0;
}
