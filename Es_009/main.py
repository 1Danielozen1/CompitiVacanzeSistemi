import time, _thread, machine
from machine import Pin

global allarm

def buzzer():
  buzzer = Pin(5, Pin.OUT)
  while allarm == 1:
    buzzer.value(1)

  buzzer.value(0)
  

_thread.start_new_thread(buzzer, ())

button = Pin(18, Pin.IN)
value = button.value()
while True:
  if button.value()==1:
    allarm = 1
  else:
    allarm = 0