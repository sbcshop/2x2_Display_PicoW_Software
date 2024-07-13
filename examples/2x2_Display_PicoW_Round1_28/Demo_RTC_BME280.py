''' Demo Code to Test onboard DS3231 RTC and BME280 Sensor '''
import random
from machine import Pin, SPI,I2C
import time
import bme280

address = 0x68
register = 0x00

i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=40000)#all sensor connected through I2C

#sec min hour week day month year
CurrentTime = b'\x40\x39\x12\x05\x30\x05\x24' #00:00:10 friday 03/03/2022 
week  = ["Sun","Mon","Tues","Wed","Thur","Fri","Sat"];

def PicoRTCSetTime():
    i2c.writeto_mem(int(address),int(register),CurrentTime)

def PicoRTCReadTime():
    return i2c.readfrom_mem(int(address),int(register),7);
  
    

bme = bme280.BME280(i2c=i2c) #pressure,temperature and humidity sensor

PicoRTCSetTime() #You can remove this line once time is set

def clock():
    data = PicoRTCReadTime()
    #print(data)
    a = data[0]&0x7F  #sec
    b = data[1]&0x7F  #min
    c = data[2]&0x3F  #hour
    d = data[3]&0x07  #week
    e = data[4]&0x3F  #day
    f = data[5]&0x1F  #month
    g = data[6]&0x3F #year
    #dt = "20%x/%02x/%02x %02x:%02x:%02x %s" %(g,f,e,c,b,a,week[d-1])
    t = "%02x:%02x:%02x" %(c,b,a)
    d = "%02x/%02x/20%x"%(e,f,g)
    print(t) #year,month,day,hour,min,sec,week
    print(d)
    #tft1.text(font,d, 40,60,st7789.YELLOW)
    #tft1.fill_rect(0, 100, 240,8, st7789.RED)
    
    time.sleep(1)
    


while 1:
    press = bme.pressure # we use only pressure from BME sensor, you can also read temperature and humidity as ewll
    humid = bme.humidity
    temp = bme.temperature
    
    print("Prssure  ",press)
    print("Temperature = ",temp)
    print("humidity = ",humid)
    
    
    time.sleep(0.01)
    
    clock()




    
    
