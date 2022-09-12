from machine import Pin
from utime import sleep

led = Pin(1, Pin.OUT)

while True:
  led.value(1)
  sleep(0.25)
  print("Ciao Mondo!")
  led.value(0)
  sleep(0.25)

