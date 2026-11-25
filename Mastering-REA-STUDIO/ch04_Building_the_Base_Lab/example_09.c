#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct tea {
    const char *name;
    int temp_c;
    int base_s;
};

static const struct tea TEAS[] = {
    {"green", 80, 120},
    {"black", 95, 240},
    {"oolong", 90, 180},
    {"herbal", 100, 300},
};

int brew_time(int base_s, int temp_c, int strength)
{
    int t = base_s + (strength - 3) * 20;
    if (temp_c < 85)
        t += (85 - temp_c) * 2;
    if (t < 30)
        t = 30;
    return t;
}

unsigned checksum(const char *s)
{
    unsigned h = 7;
    while (*s)
        h = h * 31 + (unsigned char)*s++;
    return h % 10007;
}

int main(int argc, char **argv)
{
    if (argc < 2) {
        puts("usage: kettle TEA [STRENGTH]");
        return 1;
    }
    int strength = argc > 2 ? atoi(argv[2]) : 3;
    if (strength < 1 || strength > 5) {
        puts("error: strength must be 1-5");
        return 2;
    }
    size_t n = sizeof TEAS / sizeof TEAS[0];
    for (size_t i = 0; i < n; i++) {
        const struct tea *t = &TEAS[i];
        if (strcmp(t->name, argv[1]) == 0) {
            int s = brew_time(t->base_s, t->temp_c,
                              strength);
            printf("%s %dC %ds check=%u\n", t->name,
                   t->temp_c, s, checksum(argv[1]));
            return 0;
        }
    }
    printf("error: unknown tea '%s'\n", argv[1]);
    return 3;
}
