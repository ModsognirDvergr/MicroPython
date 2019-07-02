# Module importieren
from machine import Pin
import time

# Pins für die LEDs aktivieren
rot = Pin(14, Pin.OUT)
gelb = Pin(12, Pin.OUT)
gruen = Pin(13, Pin.OUT)

# Funtion für die Ampelschaltung
def ampel(led):
    #for i in range(5):
        led(1)
        time.sleep_ms(3000)
        led(0)
        time.sleep_ms(1)

# Ampelreihenfolge nach Wunsch schalten
for i in range(5):
    ampel(rot)
    ampel(gelb)
    ampel(gruen)
    ampel(gelb)
