""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config
import gc
import time
import vga1_bold_16x32

fg = st7789.WHITE
bg = st7789.TRANSPARENT
text_x = 20
text_y = int(170/2-32)
rect_width = 320-20-20
rect_height = 32

def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        gc.collect()
        tft.jpg('pic_5.jpg', 0, 0)
        tft.fill_rect(text_x, text_y, rect_width, rect_height, st7789.BLACK, 60)
        tft.text(vga1_bold_16x32, "Hello World!", text_x, text_y, fg, bg, 255)
        tft.show()
        gc.collect()

    except BaseException as err:
        err_type = err.__class__.__name__
        print('Err type:', err_type)
        from sys import print_exception
        print_exception(err)

    finally:
        tft.deinit()
        print("tft deinit")


main()
