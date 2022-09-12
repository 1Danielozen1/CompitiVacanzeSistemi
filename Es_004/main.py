from machine import Pin
from utime import sleep

led_R = Pin(3, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_DOWN)

while True:
  if button.value() == 1:
    led_R.value(1)
  else:
    led_R.value(0)  
