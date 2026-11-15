FONT = [0xF0, 0x90, 0x90, 0x90, 0xF0,   # 0
        0x20, 0x60, 0x20, 0x20, 0x70,   # 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0,   # 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0,   # 3
        0x90, 0x90, 0xF0, 0x10, 0x10]   # 4

class Chip8:
    def __init__(self, program):
        self.mem = bytearray(4096)
        self.mem[0:len(FONT)] = bytes(FONT)
        self.mem[0x200:0x200 + len(program)] = program
        self.v = [0] * 16            # registers V0..VF
        self.i, self.pc = 0, 0x200
        self.screen = [[0] * 64 for _ in range(32)]

    def step(self):
        hi, lo = self.mem[self.pc], self.mem[self.pc + 1]
        op = hi << 8 | lo
        self.pc += 2                       # fetch
        x, y = (op >> 8) & 0xF, (op >> 4) & 0xF
        nn, nnn = op & 0xFF, op & 0xFFF
        kind = op >> 12                    # decode
        if op == 0x00E0:                   # execute
            self.screen = [[0] * 64 for _ in range(32)]
        elif kind == 0x1:
            self.pc = nnn                  # jump
        elif kind == 0x6:
            self.v[x] = nn                 # set register
        elif kind == 0x7:
            self.v[x] = (self.v[x] + nn) & 0xFF
        elif kind == 0xA:
            self.i = nnn
        elif kind == 0xF and nn == 0x29:
            self.i = self.v[x] * 5         # font address
        elif kind == 0xD:
            self.draw(self.v[x], self.v[y], op & 0xF)
        else:
            raise ValueError(f"opcode {op:04X} not built")

    def draw(self, x, y, rows):
        self.v[0xF] = 0
        for r in range(rows):
            bits = self.mem[self.i + r]
            for c in range(8):
                if bits & (0x80 >> c):
                    px, py = (x + c) % 64, (y + r) % 32
                    if self.screen[py][px]:
                        self.v[0xF] = 1    # collision
                    self.screen[py][px] ^= 1

# Our own tiny program: draw the digits 4 and 2
prog = bytes([0x00, 0xE0,   # clear the screen
              0x60, 0x01,   # V0 = 1 (x)
              0x61, 0x01,   # V1 = 1 (y)
              0x62, 0x04,   # V2 = 4
              0xF2, 0x29,   # I = font for V2
              0xD0, 0x15,   # draw 5 rows at (V0, V1)
              0x70, 0x06,   # V0 += 6
              0x62, 0x02,   # V2 = 2
              0xF2, 0x29,   # I = font for V2
              0xD0, 0x15,   # draw
              0x12, 0x14])  # jump here forever (halt)
cpu = Chip8(prog)
for _ in range(11):
    cpu.step()
for row in cpu.screen[0:7]:
    print("".join("#" if p else "." for p in row[:14]))
print(f"PC=0x{cpu.pc:03X}  V0={cpu.v[0]}  I={cpu.i}")
