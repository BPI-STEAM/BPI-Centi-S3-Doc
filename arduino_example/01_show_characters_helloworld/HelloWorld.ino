#include <Arduino_GFX_Library.h>


Arduino_DataBus *bus = new Arduino_ESP32LCD8(5 /* DC */, 4 /* CS */, 6 /* WR */, 7 /* RD */, 8 /* D0 */, 9 /* D1 */, 10 /* D2 */, 11 /* D3 */,
                                             12 /* D4 */, 13 /* D5 */, 14 /* D6 */, 15 /* D7 */);
Arduino_GFX *gfx = new Arduino_ST7789(bus, 3 /* RST */, 1 /* rotation */, true /* IPS */, 170 /* width */, 320 /* height */, 35 /* col offset 1 */,
                                      0 /* row offset 1 */, 35 /* col offset 2 */, 0 /* row offset 2 */);


#define GFX_BL 2 // default backlight pin, you may replace DF_GFX_BL to actual backlight pin

void setup(void)
{
    gfx->begin();
    gfx->fillScreen(BLACK);

#ifdef GFX_BL
    pinMode(GFX_BL, OUTPUT);
    digitalWrite(GFX_BL, HIGH);
#endif

    gfx->setCursor(10, 10);
    gfx->setTextColor(RED);
    gfx->setTextSize(2 /* x scale */, 2 /* y scale */, 2 /* pixel_margin */);
    gfx->println("Hello World!");

    delay(5000); // 5 seconds
}

void loop()
{
    gfx->setCursor(random(gfx->width()), random(gfx->height()));
    gfx->setTextColor(random(0xffff), random(0xffff));
    gfx->setTextSize(random(6) /* x scale */, random(6) /* y scale */, random(2) /* pixel_margin */);
    gfx->println("Hello World!");

    delay(1000); // 1 second
}
