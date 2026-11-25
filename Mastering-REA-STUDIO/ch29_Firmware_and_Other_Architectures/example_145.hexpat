#pragma endian little

struct FwHeader {
    char magic[4];
    u16 version;
    u16 reserved;
    u32 fs_offset;
    u32 fs_size;
    u32 fs_crc32;
};

FwHeader header @ 0x00;
