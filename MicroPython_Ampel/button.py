import machine
button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if not button.value():
        print('Button pressed!')
