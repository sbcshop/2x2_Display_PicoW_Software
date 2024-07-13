''' Display Testing Demo '''

from machine import Pin, SPI
import random
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font
import vga1_8x16 as font1
from time import sleep

#define and configure display SPI interface
spi0 = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))
spi1 = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
spi2 = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
spi3 = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))


# Define TFT displays with different CS pins
tft0 = st7789.ST7789(spi0, 240, 240, cs=Pin(28, Pin.OUT), dc=Pin(16, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=145)
tft1 = st7789.ST7789(spi1, 240, 240, cs=Pin(13, Pin.OUT), dc=Pin(12, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=145)
tft2 = st7789.ST7789(spi2, 240, 240, cs=Pin(5, Pin.OUT), dc=Pin(4, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=145)
tft3 = st7789.ST7789(spi3, 240, 240, cs=Pin(9, Pin.OUT), dc=Pin(8, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=145)

#initialize tft display
tft0.init()
tft1.init()
tft2.init()
tft3.init()


def clear_text(tft, x, y, width, height):
  """Clears a rectangular area on the TFT display."""
  tft.fill(bg, x, y, width, height)


# clear display
tft0.fill(0)
tft1.fill(0)
tft2.fill(0)
tft3.fill(0)

# fill color 
tft0.fill(st7789.RED)
tft1.fill(st7789.YELLOW)
tft2.fill(st7789.WHITE)
tft3.fill(st7789.BLUE)

while True:
    for rotation in range(4):
        fg = st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8))

        bg = st7789.color565(
            random.getrandbits(8),
            random.getrandbits(8),
            random.getrandbits(8))
        
        tft0.rotation(rotation)
        tft1.rotation(rotation)
        tft2.rotation(rotation)
        tft3.rotation(rotation)
        
        tft0.text(font, "TFT0", 50, 50, fg, bg)
        tft1.text(font, "TFT1", 40, 40, fg, bg)
        tft2.text(font, "TFT2", 60, 60, fg, bg)
        tft3.text(font, "TFT3", 70, 70, fg, bg)
        
        sleep(0.1)
        
