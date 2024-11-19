# Pinout Information
# Neopixel | Raspberry Pi Pico 
#       5V | 3V3 or 5V(VBUS)
#      Din | GP28
#      GND | GND

import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(28), 8)

n = np.n

while True:
    for i in range(10, 2 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, val)
            
            time.sleep_ms(5)
            np.write()     
