from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.ALL_CLOCKS, loop=False, delay=100)
        display.show(str(random.randint(1, 6)))
