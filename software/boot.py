# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import os

import machine
from network import WLAN

# repl on serial first
os.dupterm(machine.UART(0, 115200))

# now wifi
wlan = WLAN()

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    wlan.ifconfig(config=('192.168.1.254', '255.255.255.0', '192.168.1.1', '192.168.1.1'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('***REMOVED***', auth=(WLAN.WPA2, '***REMOVED***'), timeout=5000)
    while not wlan.isconnected():
        machine.idle()
