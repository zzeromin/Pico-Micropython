from machine import Pin, PWM
from time import sleep

led = PWM(Pin(22))

led.freq(1000)

while True:
    for duty in range(65535):
        led.duty_u16(duty)
        sleep(0.0001)
        
    for duty in range(65535, 0, -1):
        led.duty_u16(duty)
        sleep(0.0001)
