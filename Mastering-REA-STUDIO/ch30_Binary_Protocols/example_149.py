import socket
import struct
import sys


def call(sock, mtype, payload=b""):
    head = struct.pack(">2sBBH", b"KB", 1, mtype,
                       len(payload))
    sock.sendall(head + payload)
    rhead = sock.recv(6)
    _, _, rtype, size = struct.unpack(">2sBBH", rhead)
    return rtype, sock.recv(size)


with socket.create_connection(("127.0.0.1", 8900)) as s:
    rtype, data = call(s, 1)
    print("LIST", rtype, data.hex(" "))
    kind, strength = int(sys.argv[1]), int(sys.argv[2])
    rtype, data = call(s, 2, bytes([kind, strength]))
    status, secs = struct.unpack(">BH", data)
    print("BREW", rtype, status, secs)
