""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config
import gc
import time

pic_list = ["pic_1.jpg", "pic_2.jpg", "pic_3.jpg", "pic_4.jpg", "pic_5.jpg"]


def main():
    try:
        tft = tft_config.config(rotation=1)
        tft.init()
        while True:
            for pic in pic_list:
                tft.jpg(pic, 0, 0)
                tft.show()
                gc.collect()
                time.sleep(1)

    except BaseException as err:
        err_type = err.__class__.__name__
        print('Err type:', err_type)
        from sys import print_exception
        print_exception(err)

    finally:
        tft.deinit()
        print("tft deinit")


main()
