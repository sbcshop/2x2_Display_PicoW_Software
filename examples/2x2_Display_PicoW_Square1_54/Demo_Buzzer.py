from machine import Pin, PWM
import time

# Define buzzer pin
buzzer_pin = Pin(22, Pin.OUT)

def play_tone(frequency, duration):
  """Plays a tone of a certain frequency for a specified duration."""
  pwm = PWM(buzzer_pin)
  pwm.freq(frequency)
  pwm.duty_u16(5000)  # Set duty cycle (volume) to 50%
  time.sleep(duration)
  pwm.duty_u16(0)  # Stop the sound by setting duty cycle to 0
  pwm.deinit()  # Release the PWM channel

# Example usage: Play a 1 kHz tone for 1 second
#play_tone(1000, 1)

# Loop to continuously play a tone with a short pause
while True:
  play_tone(2000, 0.5)  # Play a 2000 Hz tone for 0.5 seconds
  time.sleep(0.5)  # Pause for 0.5 seconds
