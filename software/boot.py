# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import os

import machine
from network import WLAN

# disable LED matrix first
latch = machine.Pin('GP13', mode=machine.Pin.OUT)
latch.value(0)

spi = machine.SPI(0, mode=machine.SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
spi.write(b'\x00\x00\x00\x00')
latch.value(1)

# repl on serial
os.dupterm(machine.UART(0, 115200))

# now wifi
wlan = WLAN()

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    wlan.ifconfig(config=('192.168.1.254', '255.255.255.0', '192.168.1.1', '192.168.1.1'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('XXX', auth=(WLAN.WPA2, 'XXX'), timeout=5000)
    while not wlan.isconnected():
        machine.idle()
