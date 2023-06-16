""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config
import gc

def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        gc.collect()
        tft.jpg('pic_5.jpg', 0, 0)
        tft.fill_rect(20, int(170/2-32), 320-20-20, 32, st7789.BLACK, 60)
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
