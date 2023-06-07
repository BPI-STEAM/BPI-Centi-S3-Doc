Based on :
* esp-idf 4.4.3 https://github.com/espressif/esp-idf/tree/v4.4.3

* micropython https://github.com/micropython/micropython

* russhughes/st7789s3_esp_lcd https://github.com/russhughes/st7789s3_esp_lcd

# Firmware info

1. micropython1.19.1_esp32s3_qspram_st7789s3.bin
    * micropython 1.19.1 release tag
    * esp32s3, Quad SPIRAM, 8M flash
    * russhughes/st7789s3_esp_lcd
2. micropython1.20.0dev_esp32s3_qspram_st7789s3.bin
    * micropython 1.20.0 master dev, until June 6, 2023(mip, espnow)
    * esp32s3, Quad SPIRAM, 8M flash
    * russhughes/st7789s3_esp_lcd

# How to flash

## Set firmware download mode

There are two methods of operation:

1. Connect to the computer via USB, press and hold the BOOT button, then press the RESET button and release it, and finally release the BOOT button.

2. Press and hold the BOOT button when the power supply is disconnected, then connect to the computer via USB, and finally release the BOOT button.

It can be seen from this that the chip selects the startup mode when reset or re-powered through the GPIO0 controlled by the BOOT key.

Confirm the COM interface in the device manager. The serial number of the COM interface in the firmware download mode and the normal mode is usually different.

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
python -m esptool --chip esp32s3 --port COM1 --baud 460800 --before=usb_reset --after=no_reset write_flash 0x0 micropython1.19.1_esp32s3_qspram_st7789s3.bin
```
