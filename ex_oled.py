# First: install package micropython-ssd1306
# https://github.com/stlehmann/micropython-ssd1306

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# OLED 모듈의 핀 설정(SDA 8번, SCL 9번)
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(128, 64, i2c)

# OLED 모듈 초기화
oled.fill(1)
oled.show()
time.sleep(1)

oled.fill(0)
oled.show()

# OLED 모듈에 문자열 출력
oled.text("Hello, world!", 0, 0)
oled.show()
