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
fg = st7789.BLACK
bg = st7789.WHITE
text_x = 10
text_y = 10

def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        tft.fill(st7789.WHITE)
        tft.text(vga1_8x16, "Hello World!", text_x, text_y, fg, bg, 255)
        tft.text(vga1_bold_16x32, "MicroPython!", text_x, text_y+16, fg, bg, 255)
        tft.text(vga1_8x16, "vga1_8x16", text_x, text_y+16+32, fg, bg, 255)
        tft.text(vga1_bold_16x32, "vga1_bold_16x32",
                 text_x, text_y+16+32+16, fg, bg, 255)
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
