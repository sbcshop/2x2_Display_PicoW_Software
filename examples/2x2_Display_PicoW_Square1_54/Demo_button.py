''' Demo code for onboard Programmable Buttons '''

from machine import Pin, PWM
import time

# Button interfacing pin as INPUT
button1 = Pin(15, Pin.IN, Pin.PULL_UP)
button2 = Pin(27, Pin.IN, Pin.PULL_UP)
button3 = Pin(26, Pin.IN, Pin.PULL_UP)

# Define buzzer pin for OUTPUT
buzzer_pin = Pin(22, Pin.OUT)

def play_tone(frequency, duration):
  """Plays a tone of a certain frequency for a specified duration."""
  pwm = PWM(buzzer_pin)
  pwm.freq(frequency)
  pwm.duty_u16(5000)  # Set duty cycle (volume) to 50%
  time.sleep(duration)
  pwm.duty_u16(0)  # Stop the sound by setting duty cycle to 0
  pwm.deinit()  # Release the PWM channel

while 1:
    if button1.value() == 0:
        print("button 1")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
               
    elif button2.value() == 0:
        print("button 2")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
        
    elif button3.value() == 0:
        print("button 3")
        play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
        

