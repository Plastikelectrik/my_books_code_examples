#include <stdio.h>
#include <string.h>

static unsigned char NAMES[4][8] = {
    {0x34, 0x21, 0x36, 0x36, 0x3d, 0x00},
    {0x31, 0x3f, 0x32, 0x30, 0x38, 0x00},
    {0x3c, 0x3c, 0x3f, 0x3c, 0x3d, 0x34},
    {0x3b, 0x36, 0x21, 0x31, 0x32, 0x3f},
};

static void decode(void)
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 8 && NAMES[i][j]; j++)
            NAMES[i][j] ^= 0x53;
}

int main(void)
{
    decode();
    for (int i = 0; i < 4; i++)
        printf("%s\n", (char *)NAMES[i]);
    return 0;
}
