from machine import Pin
from time import sleep

led1 = Pin(22, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(16, Pin.OUT)

while True:
    led1.low()
    led2.low()
    led3.low()
    
    led3.high()
    sleep(2)
    led3.low()
    sleep(0.5)
    
    led2.high()
    sleep(1)
    led2.low()
    sleep(1)
    
    led1.high()
    sleep(2)
    led1.low()
    sleep(0.5)

