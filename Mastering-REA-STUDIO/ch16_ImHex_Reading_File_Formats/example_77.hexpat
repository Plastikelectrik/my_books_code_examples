#pragma endian little
import std.core;

struct Recipe {
    u8 kind [[comment("0 green .. 3 herbal")]];
    u8 temp_c [[comment("degrees Celsius")]];
    u16 seconds [[comment("brew time")]];
    char name[12] [[comment("NUL padded ASCII")]];
};

struct KtlFile {
    char magic[4];
    std::assert(magic == "KTL1", "bad magic");
    u16 version;
    std::assert(version == 2, "unknown version");
    u16 count;
    Recipe recipes[count];
    u32 checksum [[color("FF8000")]];
};

KtlFile file @ 0x00;
