''' Demo Code for BME280 Sensor to read Temperature, Pressure & Humidity '''
import time
from machine import I2C, Pin
import bme280

i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=40000) #all sensor connected through I2C

# create BME280 sensor class instance 
bme = bme280.BME280(i2c=i2c) 

'''
#Uncomment function to compensate temperature and humidity
#you will see difference in actual reading when running 4 TFT due to pcb heat variation
def compensate_temp(temp):
    temp = temp.replace("C"," ",1)
    vaerdi = float(temp) - 4.0
    temp = '%.1fC' % vaerdi
    return temp

def compensate_humid(humid):
    humid = humid.replace("%"," ",1)
    vaerdi = float(humid) #50% ændring ved 15grc
    vaerdi = vaerdi + ((50.0 / 15.0)*4.0)
    humid = '%.1f%%' % vaerdi
    return humid
'''

while True:
     # To read temperature, pressure and Humidity
     temperature = bme.temperature 
     #compTemp = compensate_temp(temperature)
     pressure = bme.pressure 
     humidity = bme.humidity
    
     #print the readings
     print("\nMeasurement Values are:")
     print("Prssure = ",pressure)
     print("Temp = ",temperature)
     #print("Compensated Temp = ", compTemp)
     print("humidity = ",humidity)
     
     time.sleep(0.5) # wait for half second



