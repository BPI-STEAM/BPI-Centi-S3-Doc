""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config
import vga1_8x16
import vga1_bold_16x32

"""
These default colors can be used:
BLACK           BLUE            CYAN            GREEN
MAGENTA         RED             YELLOW          WHITE
TRANSPARENT

Custom RGB colors:
color565(255,255,255)
"""
fg = st7789.RED
bg = st7789.TRANSPARENT
text_x = 10
text_y = 50

def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        tft.fill(st7789.WHITE)
        tft.text(vga1_8x16, "Hello World!", text_x-1, text_y-1, fg, bg, 205)
        tft.text(vga1_bold_16x32, "MicroPython!", text_x-2, text_y+16-2, fg, bg, 205)
        tft.text(vga1_8x16, "Hello World!", text_x, text_y, fg, bg, 255)
        tft.text(vga1_bold_16x32, "MicroPython!", text_x, text_y+16, fg, bg, 255)
        tft.show()

    except BaseException as err:
        err_type = err.__class__.__name__
        print('Err type:', err_type)
        from sys import print_exception
        print_exception(err)

    finally:
        tft.deinit()
        print("tft deinit")


main()
