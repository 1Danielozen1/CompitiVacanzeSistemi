from machine import Pin
from utime import sleep

led = Pin(5, Pin.OUT)

while True:
  led.toggle()
  print("Hello World! \n")
  sleep(0.25)