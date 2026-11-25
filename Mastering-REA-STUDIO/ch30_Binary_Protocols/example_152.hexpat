#pragma endian big

struct Header {
    char magic[2];
    u8 version;
    u8 type;
    u16 length;
};

struct Message {
    Header header;
    u8 payload[header.length];
};

Message msg @ 0x00;
