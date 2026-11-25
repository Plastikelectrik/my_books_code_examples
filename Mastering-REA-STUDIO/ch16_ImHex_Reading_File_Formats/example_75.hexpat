#pragma endian little

enum Kind : u8 {
    Green = 0, Black = 1, Oolong = 2, Herbal = 3
};

struct Recipe {
    Kind kind;
    u8 temp_c;
    u16 seconds;
    char name[12];
};

struct KtlFile {
    char magic[4];
    u16 version;
    u16 count;
    Recipe recipes[count];
    u32 checksum;
};

KtlFile file @ 0x00;
