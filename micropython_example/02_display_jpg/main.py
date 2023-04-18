""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config
import time
import gc

def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        tft.jpg("pic_1.jpg", 0, 0)
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
