""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
from machine import freq


def config(rotation=0, options=0):

    return st7789.ST7789(
        170,
        320,
        15, 14, 13, 12, 11, 10, 9, 8,
        wr=6,
        rd=7,
        reset=3,
        dc=5,
        cs=4,
        backlight=2,
        power=2,
        rotation=rotation,
        options=options)

freq(240_000_000)  # Set esp32s3 cpu frequency to 240MHz
