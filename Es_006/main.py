from machine import Pin
from utime import sleep
from machine import ADC

MAX_NUM = 65535

led_1 = Pin(0, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(2, Pin.OUT)
led_4 = Pin(3, Pin.OUT)
led_5 = Pin(4, Pin.OUT)
led_6 = Pin(5, Pin.OUT)
pot = ADC(28)

while True:
  value = pot.read_u16()/MAX_NUM;
  if value < 0.16:
    led_1.value(1)
    led_2.value(0)
    led_3.value(0)
    led_4.value(0)
    led_5.value(0)
    led_6.value(0)
  elif value > 0.16 and value <= 0.32:
    led_1.value(1)
    led_2.value(1)
    led_3.value(0)
    led_4.value(0)
    led_5.value(0)
    led_6.value(0)
  elif value > 0.32 and value <= 0.48:
    led_1.value(1)
    led_2.value(1)
    led_3.value(1)
    led_4.value(0)
    led_5.value(0)
    led_6.value(0)
  elif value > 0.48 and value <= 0.64:
    led_1.value(1)
    led_2.value(1)
    led_3.value(1)
    led_4.value(1)
    led_5.value(0)
    led_6.value(0)
  elif value > 0.64 and value <= 0.80:
    led_1.value(1)
    led_2.value(1)
    led_3.value(1)
    led_4.value(1)
    led_5.value(1)
    led_6.value(0)
  elif value > 0.80 and value <= 1:
    led_1.value(1)
    led_2.value(1)
    led_3.value(1)
    led_4.value(1)
    led_5.value(1)
    led_6.value(1)


