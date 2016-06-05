# -*- coding: utf-8 -*-

"""
LED Matrix.

      01234567890
    0 ESKISTAFUNF
    1 ZEHNZWANZIG
    2 DREIVIERTEL
    3 VORFUNKNACH
    4 HALBAELFUNF
    5 EINSXAMZWEI
    6 DREIAUJVIER
    7 SECHSNLACHT
    8 SIEBENZWOLF
    9 ZEHNEUNKUHR
      01234567890
"""

try:
    import ustruct as struct
except ImportError:
    import struct

R0 = 1
R1 = R0 << 1
R2 = R1 << 1
R3 = R2 << 1
R4 = R3 << 1
R5 = R4 << 1
R6 = R5 << 1
R7 = R6 << 1
R8 = R7 << 1
R9 = R8 << 1


class Matrix:
    """LED Matrix wrapper."""

    # 2 bytes for all columns + 2 bytes for all rows (shift register on cathode are inverted)
    off = b'\x00\x00\xff\xff'

    def __init__(self):
        self._current_col = 0
        self.columns = []
        self.reset()

    def _set(self, cols, value):
        for c in cols:
            self._m[c] = self._m[c] | value

    def reset(self):
        self._m = [0] * 11

    def vor(self):
        self._set([0, 1, 2], R3)

    def nach(self):
        self._set([7, 8, 9, 10], R3)

    def es_ist(self):
        self._set([0, 1, 3, 4, 5], R0)

    def uhr(self):
        self._set([8, 9, 10], R9)

    def fuenf(self):
        self._set([7, 8, 9, 10], R0)

    def zehn(self):
        self._set([0, 1, 2, 3], R1)

    def viertel(self):
        self._set([4, 5, 6, 7, 8, 9, 10], R2)

    def zwanzig(self):
        self._set([4, 5, 6, 7, 8, 9, 10], R1)

    def halb(self):
        self._set([0, 1, 2, 3], R4)

    def dreiviertel(self):
        self._set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], R2)

    def h_ein(self):
        self._set([0, 1, 2], R5)

    def h_eins(self):
        self._set([0, 1, 2, 3], R5)

    def h_zwei(self):
        self._set([7, 8, 9, 10], R5)

    def h_drei(self):
        self._set([0, 1, 2, 3], R6)

    def h_vier(self):
        self._set([7, 8, 9, 10], R6)

    def h_fuenf(self):
        self._set([7, 8, 9, 10], R4)

    def h_sechs(self):
        self._set([0, 1, 2, 3, 4], R7)

    def h_sieben(self):
        self._set([0, 1, 2, 3, 4, 5], R8)

    def h_acht(self):
        self._set([7, 8, 9, 10], R8)

    def h_neun(self):
        self._set([3, 4, 5, 6], R9)

    def h_zehn(self):
        self._set([0, 1, 2, 3], R9)

    def h_elf(self):
        self._set([5, 6, 7], R4)

    def h_zwoelf(self):
        self._set([6, 7, 8, 9, 10], R8)

    def done(self):
        self.columns = [struct.pack('<HH', 1 << i, v ^ 2 ** 16 - 1) for i, v in enumerate(self._m) if v > 0]

    def debug(self):
        for r in range(0, 10):
            for c in self._m:
                print("{0:{fill}16b}".format(c, fill='0')[-r - 1], end='')  # noqa
            print()
        print()


def clock2matrix(hour, minute):
    m = Matrix()
    m.es_ist()

    exact = False

    # set minute
    minute_interval = minute // 5
    if minute_interval == 0:
        # XX:00
        exact = True
    elif minute_interval == 1:
        # XX:05
        m.fuenf()
        m.nach()
    elif minute_interval == 2:
        # XX:10
        m.zehn()
        m.nach()
    elif minute_interval == 3:
        # XX:15
        m.viertel()
        hour += 1
    elif minute_interval == 4:
        # XX:20
        m.zwanzig()
        m.nach()
    elif minute_interval == 5:
        # XX:25
        m.fuenf()
        m.vor()
        m.halb()
        hour += 1
    elif minute_interval == 6:
        # XX:30
        m.halb()
        hour += 1
    elif minute_interval == 7:
        # XX:35
        m.fuenf()
        m.nach()
        m.halb()
        hour += 1
    elif minute_interval == 8:
        # XX:40
        m.zehn()
        m.nach()
        m.halb()
        hour += 1
    elif minute_interval == 9:
        # XX:45
        m.dreiviertel()
        hour += 1
    elif minute_interval == 10:
        # XX:50
        m.zehn()
        m.vor()
        hour += 1
    elif minute_interval == 11:
        # XX:55
        m.fuenf()
        m.vor()
        hour += 1

    # set hour
    if exact:
        m.uhr()

    if hour in [0, 12, 24]:
        m.h_zwoelf()
    elif hour in [1, 13]:
        if exact:
            m.h_ein()
        else:
            m.h_eins()
    elif hour in [2, 14]:
        m.h_zwei()
    elif hour in [3, 15]:
        m.h_drei()
    elif hour in [4, 16]:
        m.h_vier()
    elif hour in [5, 17]:
        m.h_fuenf()
    elif hour in [6, 18]:
        m.h_sechs()
    elif hour in [7, 19]:
        m.h_sieben()
    elif hour in [8, 20]:
        m.h_acht()
    elif hour in [9, 21]:
        m.h_neun()
    elif hour in [10, 22]:
        m.h_zehn()
    elif hour in [11, 23]:
        m.h_elf()

    # we are done
    m.done()

    return m


if __name__ == '__main__':
    # matrix = Matrix()
    # matrix.es_ist()
    # matrix.dreiviertel()
    # matrix.vor()
    # matrix.nach()
    # matrix.h_vier()
    # matrix.uhr()
    # matrix.dreiviertel()
    # matrix.vor()
    # matrix.nach()
    # matrix.h_vier()
    # matrix.fuenf()
    # matrix.debug()

    matrix = clock2matrix(1, 0)
    matrix.debug()
    matrix = clock2matrix(1, 5)
    matrix.debug()
    matrix = clock2matrix(1, 10)
    matrix.debug()
    matrix = clock2matrix(1, 15)
    matrix.debug()
    matrix = clock2matrix(1, 20)
    matrix.debug()
    matrix = clock2matrix(1, 25)
    matrix.debug()
    matrix = clock2matrix(1, 30)
    matrix.debug()
    matrix = clock2matrix(1, 35)
    matrix.debug()
    matrix = clock2matrix(1, 40)
    matrix.debug()
    matrix = clock2matrix(1, 45)
    matrix.debug()
    matrix = clock2matrix(1, 50)
    matrix.debug()
    matrix = clock2matrix(1, 55)
    matrix.debug()
