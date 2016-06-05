# -*- coding: utf-8 -*-
try:
    import usocket as socket
except:
    import socket


def write_word(value, d, clk, lat):
    bits = [value >> i & 1 for i in range(31, -1, -1)]
    print(bits)
    for i in range(len(bits) - 1, -1, -1):
        d.value(bits[i])
        clk.value(1)
        clk.value(0)

    lat.value(1)
    lat.value(0)


def update(file="main.py"):
    s = socket.socket()

    ai = socket.getaddrinfo("192.168.1.101", 8000)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)
    s = s.makefile("rwb", 0)
    s.write(b"GET /{} HTTP/1.0\n\n".format(file))
    open(file, "w").write(s.read())
