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
    temp = temp.replace("C"," ",1)  # Remove the "C" from the temperature string
    vaerdi = float(temp) - 4.0  # Subtract 4.0 from the temperature value
    temp = '%.1fC' % vaerdi  # Format the adjusted value back to a string with "C"
    return temp

def compensate_humid(humid):
    humid = humid.replace("%"," ",1)  # Remove the "%" from the humidity string
    vaerdi = float(humid)  # Convert the value to a float
    vaerdi = vaerdi + ((50.0 / 15.0)*4.0)  # Adjust the value based on a 50% change for a 15°C increase
    humid = '%.1f%%' % vaerdi  # Format the adjusted value back to a string with "%"
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



