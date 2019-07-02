from machine import Pin
import time

gruen = Pin(14, Pin.OUT)
gelb = Pin(12, Pin.OUT)
rot = Pin(13, Pin.OUT)
button = Pin(5, Pin.IN, Pin.PULL_UP)

def ampel(led):
        led(1)
        time.sleep_ms(3000)
        led(0)
        time.sleep_ms(1)

while True:
    if not button.value():
        ampel(gelb)
        ampel(gruen)
    else:
        ampel(rot)
