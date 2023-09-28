""" BPI-Centi-S3 170x320 ST7789 display """

"""
These default colors can be used:
BLACK           BLUE            CYAN            GREEN
MAGENTA         RED             YELLOW          WHITE
TRANSPARENT

Custom RGB colors:
color565(255,255,255)
"""

import st7789
import vga1_8x16
import tft_config
from rotary_irq_esp import RotaryIRQ
from button_irq import Button
import gc
import time


def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]

    def new_func(*args, **kwargs):
        t = time.ticks_us()
        result = f(*args, **kwargs)
        delta = time.ticks_diff(time.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta / 1000))
        return result

    return new_func


class TextRect:
    def __init__(self):
        self.tft = None
        self.text_y = None
        self.text_x = None
        self.rect_height = None
        self.rect_width = None

    def rect(self, tft, font, text, text_coord,fg, bg, alpha_text, alpha_rect):
        self.tft = tft
        self.rect_width = font.WIDTH * len(text)
        self.rect_height = font.HEIGHT
        self.text_x = text_coord[0]
        self.text_y = text_coord[1]
        self.tft.fill_rect(self.text_x, self.text_y,
                           self.rect_width, self.rect_height, bg, alpha_rect)
        self.tft.text(font, text, self.text_x, self.text_y,
                      fg, -1, alpha_text)

    def erase(self, bg):
        buffer, _, _ = self.tft.jpg_decode(bg, self.text_x, self.text_y, self.rect_width, self.rect_height)
        self.tft.blit_buffer(buffer, self.text_x, self.text_y, self.rect_width, self.rect_height)


class MenuBar:
    def __init__(self, tft, font, text_list, text_coord, spacing, jpg, fg, bg, alpha_text=255,
                 alpha_rect=255):
        self.tft = tft
        self.font = font
        self.text_list = text_list
        self.text_coord = text_coord
        self.spacing = spacing
        self.jpg = jpg
        self.fg = fg
        self.bg = bg
        self.alpha_text = alpha_text
        self.alpha_rect = alpha_rect
        self.last_selected = None
        self.menu_bar = {}
        self.jpg_decode_buffer = {}
        self.jpg_decoded = False

    @timed_function
    # @micropython.native
    def get_menu_bar(self):
        for i, j in zip(self.text_list, range(len(self.text_list))):
            text_coord = (self.text_coord[0], self.text_coord[1] + j * (self.font.HEIGHT + self.spacing))
            _temp = TextRect()
            _temp.rect(self.tft, self.font, i, text_coord, self.fg, self.bg, self.alpha_text, self.alpha_rect)
            self.menu_bar[j] = _temp
            if not self.jpg_decoded:
                # print("jpg_decoding...")
                self.jpg_decode_buffer[j] = self.tft.jpg_decode(self.jpg, text_coord[0], text_coord[1],
                                                                self.font.WIDTH * len(i), self.font.HEIGHT)
        if not self.jpg_decoded:
            self.jpg_decoded = True

    @timed_function
    def select(self, num, fg_1, bg_1, alpha_text_1=255, alpha_rect_1=255):
        if self.last_selected is not None and self.last_selected != num:
            text_coord = (self.text_coord[0],
                          self.text_coord[1] + self.last_selected * (self.font.HEIGHT + self.spacing))
            _buffer, _width, _height = self.jpg_decode_buffer.get(self.last_selected)
            self.tft.blit_buffer(_buffer, text_coord[0], text_coord[1], _width, _height)
            self.menu_bar.get(self.last_selected).rect(self.tft, self.font, self.text_list[self.last_selected],
                                                       text_coord,
                                                       self.fg, self.bg, self.alpha_text, self.alpha_rect)
        text_coord = (self.text_coord[0], self.text_coord[1] + num * (self.font.HEIGHT + self.spacing))
        _buffer, _width, _height = self.jpg_decode_buffer.get(num)
        self.tft.blit_buffer(_buffer, text_coord[0], text_coord[1], _width, _height)
        self.menu_bar.get(num).rect(self.tft, self.font, self.text_list[num], text_coord,
                                    fg_1, bg_1, alpha_text_1, alpha_rect_1)
        self.last_selected = num

    @timed_function
    def erase_all(self):
        for i in range(len(self.text_list)):
            text_coord = (self.text_coord[0], self.text_coord[1] + i * (self.font.HEIGHT + self.spacing))
            _buffer, _width, _height = self.jpg_decode_buffer.get(i)
            self.tft.blit_buffer(_buffer, text_coord[0], text_coord[1], _width, _height)

def main():
    try:
        text_x = 10
        text_y = 10
        tft = tft_config.config(rotation=1)
        text_list = [
            "pic_1.jpg",
            "pic_2.jpg",
            "pic_3.jpg",
            "pic_4.jpg",
            "pic_5.jpg",
            "pic_6.jpg",
        ]

        tft.init()
        gc.collect()
        r = RotaryIRQ(pin_num_clk=37, pin_num_dt=47, min_val=0, max_val=5, reverse=False,
                      range_mode=RotaryIRQ.RANGE_WRAP)
        b35 = Button(35)
        last_r_value = None
        tft.jpg(text_list[0], 0, 0)

        option_set = MenuBar(tft, vga1_8x16, text_list, (text_x, text_y), 2, text_list[0],
                             st7789.WHITE, st7789.BLACK, alpha_text=25, alpha_rect=125)
        option_set.get_menu_bar()
        tft.show()
        print(option_set.menu_bar)
        b35_lock_0 = 0
        last_r_selected = 0
        while True:

            if b35.count_0 == 0:
                r_value = r.value()
                if r_value != last_r_value:
                    option_set.select(r_value, st7789.BLACK, st7789.WHITE, alpha_text_1=25, alpha_rect_1=125)
                    tft.show()
                    last_r_value = r_value
                    gc.collect()
            if b35.count_0 == 1 and b35_lock_0 == 0:
                r_selected = r_value
                if r_selected != last_r_selected:
                    tft.jpg(text_list[r_selected], 0, 0)
                    tft.show()
                    option_set = MenuBar(tft, vga1_8x16, text_list, (text_x, text_y), 2, text_list[r_selected],
                                         st7789.WHITE, st7789.BLACK, alpha_text=25, alpha_rect=125)
                    option_set.get_menu_bar()
                    last_r_selected = r_selected
                else:
                    option_set.erase_all()
                    tft.show(True)
                    option_set.get_menu_bar()
                b35_lock_0 = 1
                gc.collect()
            if b35.count_0 >= 2:
                b35.count_0 = 0
                b35_lock_0 = 0
                option_set.select(last_r_selected, st7789.BLACK, st7789.WHITE, alpha_text_1=25, alpha_rect_1=125)
                r._value = last_r_selected  #
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
