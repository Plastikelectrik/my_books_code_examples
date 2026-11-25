import socketserver
import struct

TEAS = [(80, 120), (95, 240), (90, 180), (100, 300)]


def brew(kind, strength):
    if kind >= len(TEAS):
        return 2, 0
    if not 1 <= strength <= 5:
        return 1, 0
    temp, base = TEAS[kind]
    t = base + (strength - 3) * 20
    if temp < 85:
        t += (85 - temp) * 2
    return 0, max(t, 30)


def reply(mtype, payload):
    head = struct.pack(">2sBBH", b"KB", 1, mtype | 0x80,
                       len(payload))
    return head + payload


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            head = self.request.recv(6)
            if len(head) < 6:
                return
            magic, ver, mtype, size = struct.unpack(
                ">2sBBH", head)
            body = b""
            if size:
                body = self.request.recv(size)
            if magic != b"KB" or ver != 1:
                return
            if mtype == 1:
                out = bytes([len(TEAS)])
                for i, row in enumerate(TEAS):
                    rec = struct.pack(">BBH", i, *row)
                    out += rec
                self.request.sendall(reply(1, out))
            elif mtype == 2 and len(body) == 2:
                status, secs = brew(body[0], body[1])
                out = struct.pack(">BH", status, secs)
                self.request.sendall(reply(2, out))
            else:
                self.request.sendall(reply(0x7F, b"\x03"))


addr = ("127.0.0.1", 8900)
with socketserver.TCPServer(addr, Handler) as srv:
    srv.serve_forever()
