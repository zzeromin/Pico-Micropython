import machine
import time

led = machine.Pin(22, machine.Pin.OUT)

led.value(1)
time.sleep(1)
led.value(0)
time.sleep(1)
