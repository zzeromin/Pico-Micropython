from machine import Pin, PWM
from time import sleep

led = PWM(Pin(22))
led.freq(1000)

while True:
    for duty in range(65000):
        print(duty)
        led.duty_u16(duty)
        sleep(0.0001)
