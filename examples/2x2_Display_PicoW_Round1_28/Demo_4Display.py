''' Display Demo Run '''
from machine import Pin, SPI
import random
import gc9a01
import vga1_bold_16x32 as font
from time import sleep

spi0 = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
spi1 = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))

spi3 = SPI(0, baudrate=40000000, sck=Pin(6), mosi=Pin(7))
spi4 = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))

# Define TFT displays with different CS pins
tft0 = gc9a01.GC9A01(spi0, 240, 240, cs=Pin(5, Pin.OUT), dc=Pin(4, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=0)
tft1 = gc9a01.GC9A01(spi3, 240, 240, cs=Pin(9, Pin.OUT), dc=Pin(8, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=0)
tft2 = gc9a01.GC9A01(spi1, 240, 240, cs=Pin(13, Pin.OUT), dc=Pin(12, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=0)
tft3 = gc9a01.GC9A01(spi4, 240, 240, cs=Pin(28, Pin.OUT), dc=Pin(16, Pin.OUT), backlight=Pin(14, Pin.OUT), rotation=0)

tft0.init()
tft1.init()
tft2.init()
tft3.init()


def clear_text(tft, x, y, width, height):
  """Clears a rectangular area on the TFT display."""
  tft.fill(bg, x, y, width, height)

def random_color():
    fill = gc9a01.color565(
        random.getrandbits(8),
        random.getrandbits(8),
        random.getrandbits(8))
    return fill

tft0.fill(0)
tft1.fill(0)
tft2.fill(0)
tft3.fill(0)

sleep(1)
tft0.fill(random_color())
tft1.fill(random_color())
tft2.fill(random_color())
tft3.fill(random_color())

while True:
  for rotation in range(4):
    fg = gc9a01.color565(
        random.getrandbits(8),
        random.getrandbits(8),
        random.getrandbits(8))

    bg = gc9a01.color565(
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




