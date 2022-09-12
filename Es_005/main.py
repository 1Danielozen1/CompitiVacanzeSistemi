from machine import Pin
from utime import sleep

led_V = Pin(1, Pin.OUT)
led_G = Pin(2, Pin.OUT)
led_R = Pin(3, Pin.OUT)
button = Pin(4, Pin.IN, Pin.PULL_DOWN)

while True:
  if button.value() == 1:
    led_G.value(1)
    led_R.value(0)
    led_V.value(0)
    sleep(0.5)
    led_G.value(0)
    led_R.value(0)
    led_V.value(0)    
    sleep(0.5)
  else:
    led_V.value(1)
    led_R.value(0)
    sleep(3)
    led_G.value(1)
    sleep(1)
    led_G.value(0)
    led_V.value(0)
    led_R.value(1)
    sleep(3)
