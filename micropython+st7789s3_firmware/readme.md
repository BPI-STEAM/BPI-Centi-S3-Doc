Based on :
    esp-idf 4.4.3 https://github.com/espressif/esp-idf/tree/v4.4.3
    micropython https://github.com/micropython/micropython
    russhughes/st7789s3_esp_lcd https://github.com/russhughes/st7789s3_esp_lcd

# How to flash

## install esptool

```
python -m pip install esptool
```

## erase_flash

```
python -m esptool --chip esp32s3 --port COM1 --baud 460800 erase_flash
```

## write_flash

```
python -m esptool --chip esp32s3 --port COM1 --baud 460800 --before=usb_reset --after=no_reset write_flash 0x0 esp32s3_micropython_qspram_st7789s3_idf4.4.3.bin
```
