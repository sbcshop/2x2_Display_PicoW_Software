''' Demo Read/Write operation code to onboard microSD card'''
import sdcard
import os
from machine import UART,SPI,Pin, PWM,I2C
import time
from utime import sleep

#define and configure SPI interfacing of sdcard with Pico
spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16))

def sdtest(data):
    sd=sdcard.SDCard(spi,Pin(17))  # pass spi, CS 
    vfs = os.VfsFat(sd)
    print(vfs)
    os.mount(vfs, "/fc")
    print("Filesystem check")
    print(os.listdir("/fc"))

    fn = "/fc/File.txt"
    print()
    print("Single block read/write")
    with open(fn, "a") as f:
        n = f.write(data)  
        print(n, "bytes written")

    with open(fn, "r") as f:
        result2 = f.read()
        print(len(result2), "bytes read")

    os.umount("/fc")

while True:
    try:
        #text = input("Enter any Text")
        text = "hello"
        sdtest(text)
        sleep(5)
    
    except OSError as e:
         print("OS error: ", e)

