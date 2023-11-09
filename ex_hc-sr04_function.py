from machine import Pin, time_pulse_us
import utime

trig = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)

led = Pin(25, Pin.OUT)

def measure_distance():
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(10)
    trig.low()
    pulse_duration = time_pulse_us(echo, Pin.high)
    distance = (pulse_duration / 29) / 2  
    return distance

while True:
    distance = measure_distance()
    print(f"Distance: {distance} cm")
    
    if distance < 10:
        led.on()
    else:
        led.off()
    
    utime.sleep(1)
