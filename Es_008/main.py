from machine import Pin
from utime import sleep
from machine import ADC
from machine import PWM

led =PWM(Pin(0, Pin.OUT))
pot = ADC(28)
led.duty_u16(0);

while True:
  value = pot.read_u16();
  led.duty_u16(value)



