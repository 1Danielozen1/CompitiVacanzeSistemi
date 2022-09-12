from machine import Pin
from utime import sleep

f = 100
d = 1
ta = (d / f)*1
ts = ((1 - d)/f)*1000
led = Pin(5, Pin.OUT)

while True:
  led.value(0)
  sleep(ta)
  led.value(1)
  sleep(ts)
