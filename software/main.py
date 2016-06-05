# -*- coding: utf-8 -*-

from machine import Pin, SPI, Timer
import micropython

from led_matrix import Matrix, clock2matrix
from untplib import settime

micropython.alloc_emergency_exception_buf(1000)

TIMEZONE_OFFSET = 2
OFF = Matrix.off

# init spi interface
spi = SPI(0, mode=SPI.MASTER, bits=32, pins=('GP14', 'GP16', 'GP15'))
latch = Pin('GP22', mode=Pin.OUT)
latch.value(0)
trigger = Pin('GP5', mode=Pin.OUT)
trigger.value(0)

# all off
spi.write(OFF)
# update LEDs
latch.value(1)
latch.value(0)

# set internal clock
rtc = settime(timezone_offset=TIMEZONE_OFFSET)


def t(timer):
    trigger.toggle()
    print("timer")


def main():
    global rtc

    try:
        tim = Timer(1, mode=Timer.ONE_SHOT, width=32)

        while True:
            year, month, day, hour, minute, second, *_ = rtc.now()
            timer = tim.channel(Timer.A | Timer.B, period=(60 - second) * 1000000)
            timer.irq(handler=t, trigger=Timer.TIMEOUT)

            print(hour, minute, second)
            if hour == 4 and minute == 0 and second == 0:
                rtc = settime(timezone_offset=TIMEZONE_OFFSET)

            leds = clock2matrix(hour=hour, minute=minute).columns

            # led matrix multiplexing
            # while True:
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
    except:
        # all off
        spi.write(OFF)
        # update LEDs
        latch.value(1)
        latch.value(0)


if __name__ == '__main__':
    # main()
    pass
