open('boot.py').read()
open('main.py').read()

# import webrepl; webrepl.start(password='admin')

# import machine; machine.reset()

# tim = Timer(3, mode=Timer.PWM)
# ch = tim.channel(Timer.A, freq=100)
# ch.duty_cycle(900)

# data = Pin(Pin.board.X1, Pin.OUT_PP)
# latch = Pin(Pin.board.X2, Pin.OUT_PP)
# clock = Pin(Pin.board.X3, Pin.OUT_PP)


# data.value(0)
# latch.value(0)
# clock.value(0)


# while True:
#     write_word(0, data, clock, latch)
#     time.sleep(2)
#     write_word(2**8 - 1, data, clock, latch)
#     time.sleep(2)
#     write_word(2**16 - (2**8 - 1) - 1, data, clock, latch)
#     time.sleep(2)
#     write_word(2**16 - 1, data, clock, latch)
#     time.sleep(2)


""">>> spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> latch.value(1)
>>> latch.value(0)
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> latch.value(1)
>>> latch.value(0)
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> latch.value(1)
>>> latch.value(0)
>>> spi.write(128)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> spi.write(32768)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(128)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(128)
1
>>> spi.write(128)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(1)
1
>>> latch.value(1); latch.value(0)
>>> spi.write(64); latch.value(1); latch.value(0)
1
>>> spi.write(64); latch.value(1); latch.value(0)
1
>>> spi.write(32); latch.value(1); latch.value(0)
1
>>> spi.write(16); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(2); latch.value(1); latch.value(0)
1
>>> spi.write(3); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(4); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')

>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi))
1
>>> spi.write(1024); latch.value(1); latch.value(0)
1
>>> spi.write(512); latch.value(1); latch.value(0)
1
>>> spi.write(256); latch.value(1); latch.value(0)
1
>>> spi.write(128); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarit pins=('GP14', 'GP16', 'GParity pins=('GP14', 'GP16', 'GP15'))

>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GP15')
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=1, pins=('GP14', 'GP16', 'GPspi =
>>>
>>>
>>>
>>>
>>> spi = SPI(0, mode=SPI.MASTER, bits=32, polarity=0, phase=1, pins=('GP14', 'GP16', 'GP15'))
>>> spi.write(1); latch.value(1); latch.value(0)
1
>>> spi.write(2); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(4); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)
1
>>> spi.write(4); latch.value(1); latch.value(0)
1
>>> spi.write(0); latch.value(1); latch.value(0)

from utils import write_word
from machine import Pin

data = Pin('GP8', mode=Pin.OUT)
data.value(0)
clk = Pin('GP14', mode=Pin.OUT)
clk.value(0)
latch = Pin('GP13', mode=Pin.OUT)
latch.value(0)

from machine import SPI
spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))

# off
write_word(65535, data, clk, latch)

# A1
write_word(2147516415, data, clk, latch)
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# B1
write_word(1073774591, data, clk, latch)
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

bytearray(int('1000000010000001', 2).to_bytes(2, byteorder='big'))


class Matrix:
    def vor
        self._matrix[3] XOR 1000101001010

    def fuenf
    def h_fuenf

    __iter__
        return self._matrix

# A1
spi.write(struct.pack('>I', int('00000001000000001111111011111111', 2)))
import ustruct as struct

for i in range(0, 10000):
a = spi.write(struct.pack('>I', int('00000001000000001111111011111111', 2)))
latch.value(1); latch.value(0)
a = spi.write(0)


spi.write(0); latch.value(1); latch.value(0)



"""
