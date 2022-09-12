from machine import Pin
from utime import sleep

led_G = Pin(5, Pin.OUT)
led_V = Pin(2, Pin.OUT)
led_R = Pin(3, Pin.OUT)

while True:
  led_V.value(1)
  led_R.value(0)
  sleep(3)
  led_G.value(1)
  sleep(1)
  led_G.value(0)
  led_V.value(0)
  led_R.value(1)
  sleep(3)
