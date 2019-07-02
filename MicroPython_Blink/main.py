from machine import Pin
import time

led = Pin(2, Pin.OUT)
while True:
    led(1)
    time.sleep_ms(5000)
    led(0)
    time.sleep_ms(5000)
