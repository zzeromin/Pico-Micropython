# reference: https://github.com/rsc1975/micropython-hcsr04

from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=21, echo_pin=20)

while True:
    distance = sensor.distance_cm()
    print('거리=', distance, 'cm')
    
    time.sleep(1)
