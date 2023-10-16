from machine import Pin, ADC, PWM
from time import sleep

led = PWM(Pin(22)) # PWM 객체 생성
potentiometer = ADC(26)
led.freq(1000) # 신호 주기 설정

while True:
    value = potentiometer.read_u16()
    print(value)
    led.duty_u16(value) # PWM 신호 발생(0~65535)
    sleep(0.1)
