from machine import Pin
import utime

trigger_pin = Pin(2, Pin.OUT)
echo_pin = Pin(3, Pin.IN)

led = Pin(22, Pin.OUT)

def measure_distance():
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()
    
    while echo_pin.value() == 0:
        pulse_start = utime.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = utime.ticks_us()
    
    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration * 0.0343) / 2  

    return distance

while True:
    distance = measure_distance()
    print(f"Distance: {distance} cm")
    
    if distance < 10:
        led.on()
    else:
        led.off()
    
    utime.sleep(1)
