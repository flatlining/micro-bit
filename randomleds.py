from microbit import *
import random

def ledstatus():
    return random.randint(0, 9)

def screenstatus():
    return [
        [ledstatus(), ledstatus(), ledstatus(), ledstatus(), ledstatus()],
        [ledstatus(), ledstatus(), ledstatus(), ledstatus(), ledstatus()],
        [ledstatus(), ledstatus(), ledstatus(), ledstatus(), ledstatus()],
        [ledstatus(), ledstatus(), ledstatus(), ledstatus(), ledstatus()],
        [ledstatus(), ledstatus(), ledstatus(), ledstatus(), ledstatus()],
        ]

led = screenstatus()

while True:
    if button_a.is_pressed():
        led = screenstatus()
    elif button_b.is_pressed():
        led[random.randint(0, 4)][random.randint(0, 4)] = random.randint(0, 9)
    
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, led[x][y])
    
    sleep(0.1*1000)