from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        sleep(0.1)
