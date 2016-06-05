# -*- coding: utf-8 -*-

from machine import Pin, SPI, Timer
import micropython

from led_matrix import Matrix, clock2matrix
from untplib import settime

micropython.alloc_emergency_exception_buf(1000)

TIMEZONE_OFFSET = 2
OFF = Matrix.off

# init spi interface
latch = Pin('GP13', mode=Pin.OUT)
latch.value(0)
spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
trigger = Pin('GP5', mode=Pin.OUT)
trigger.value(0)

# set internal clock
rtc = settime(timezone_offset=TIMEZONE_OFFSET)


def main():
    global rtc

    try:
        year, month, day, hour, minute, second, *_ = rtc.now()
        # initial trigger timer
        timer = Timer(3, mode=Timer.PERIODIC, width=32)
        # timer_channel = timer.channel(Timer.A | Timer.B, period=(60 - second) * 1000000)
        timer_channel = timer.channel(Timer.A | Timer.B, period=30000000)
        timer_channel.irq(handler=lambda t: trigger.toggle(), trigger=Timer.TIMEOUT)

        while True:
            leds = clock2matrix(hour=hour, minute=minute).columns

            # led matrix multiplexing
            current_trigger = trigger.value()
            while trigger.value() == current_trigger:
                for col in leds:
                    # write current time
                    spi.write(col)
                    # update LEDs
                    latch.value(1)
                    latch.value(0)

                    # all off
                    spi.write(OFF)
                    # update LEDs
                    latch.value(1)
                    latch.value(0)

            # set new trigger timer
            year, month, day, hour, minute, second, *_ = rtc.now()

            # update rtc at 04:00
            if hour == 4 and minute == 0 and second == 0:
                rtc = settime(timezone_offset=TIMEZONE_OFFSET)
    except:
        # all off
        latch.value(0)
        spi.write(OFF)
        # update LEDs
        latch.value(1)
        latch.value(0)


if __name__ == '__main__':
    main()
    # pass
