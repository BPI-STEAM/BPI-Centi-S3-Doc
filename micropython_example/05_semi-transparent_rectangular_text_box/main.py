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


def text_rect(tft, font, font_size, text: str, text_coord,
              fg=st7789.WHITE, bg=st7789.BLACK, alpha_text=255, alpha_rect=255):
    rect_width = font_size[0] * len(text)
    rect_height = font_size[1]
    tft.fill_rect(text_coord[0], text_coord[1],
                  rect_width, rect_height, bg, alpha_rect)
    tft.text(font, text, text_coord[0], text_coord[1],
             fg, st7789.TRANSPARENT, alpha_text)


def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        gc.collect()
        tft.jpg('pic_5.jpg', 0, 0)
        text_rect(tft, vga1_bold_16x32, (16, 32), "Hello World!", (text_x, text_y),
                  fg=st7789.WHITE, bg=st7789.BLACK, alpha_text=80, alpha_rect=60)
        text_rect(tft, vga1_bold_16x32, (16, 32), "It's MicroPython!", (text_x, text_y+32),
                  fg=st7789.WHITE, bg=st7789.BLACK, alpha_text=255, alpha_rect=60)
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
