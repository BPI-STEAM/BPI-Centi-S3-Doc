""" BPI-Centi-S3 170x320 ST7789 display """

import st7789
import tft_config

tft = tft_config.config(rotation=1, options=0)
tft.init()
tft.fill(st7789.RED) 
tft.show(True)
tft.deinit()  # Deinitialize the display or it will cause a crash on the next run
