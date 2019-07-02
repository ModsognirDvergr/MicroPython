from machine import Pin
import time

rot = Pin(14, Pin.OUT)
gelb = Pin(12, Pin.OUT)
gruen = Pin(13, Pin.OUT)

for i in range(3):
    rot(1)
    time.sleep_ms(3000)
    rot(0)
    time.sleep_ms(1)

    gelb(1)
    time.sleep_ms(3000)
    gelb(0)
    time.sleep_ms(1)

    gruen(1)
    time.sleep_ms(3000)
    gruen(0)
    time.sleep_ms(1)

    gelb(1)
    time.sleep_ms(3000)
    gelb(0)
    time.sleep_ms(1)
