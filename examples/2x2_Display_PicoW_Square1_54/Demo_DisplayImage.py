''' 2x2 Display with Pico W (Square)'''

import random
import st7789
import time
from machine import Pin, SPI, PWM
import vga1_bold_16x32 as font
import vga1_8x16 as font2
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

tft0.init()
tft1.init()
tft2.init()
tft3.init()
sleep(0.1)

# Define Button pins
button1 = Pin(26, Pin.IN, Pin.PULL_UP)
button2 = Pin(27, Pin.IN, Pin.PULL_UP)
button3 = Pin(15, Pin.IN, Pin.PULL_UP)

# Define buzzer pin
buzzer_pin = Pin(22, Pin.OUT)

    
def play_tone(frequency, duration):
  """Plays a tone of a certain frequency for a specified duration."""
  print("Play Buzzer")
  pwm = PWM(buzzer_pin)
  pwm.freq(frequency)
  pwm.duty_u16(5000)  # Set duty cycle (volume) to 50%
  time.sleep(duration)
  pwm.duty_u16(0)  # Stop the sound by setting duty cycle to 0
  pwm.deinit()  # Release the PWM channel
   
fg = st7789.color565(255, 255, 0)
bg = st7789.color565(0, 0, 0)
tft1.text(font, "Press", 90, 80, fg, bg)
tft1.text(font, "Buttons", 70, 110, fg, bg)

#tft1.jpg("img/logo.jpg",0,0,st7789.FAST)
while True:
    if button1.value() == 0:
        print("button 1")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
        tft3.jpg("img/logo.jpg",0,0,st7789.FAST)

    elif button2.value() == 0:
        print("button 2")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
        tft2.jpg("img/logo.jpg",0,0,st7789.FAST)
        
    elif button3.value() == 0:
        print("button 3")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
        tft0.jpg("img/logo.jpg",0,0,st7789.FAST)
        
    time.sleep(0.2)






