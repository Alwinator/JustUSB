# Written for MicroPython, RPI Pico

import time
from machine import Pin
from neopixel import NeoPixel


def clamp(value, min_value, max_value):
    return max(min_value, min(max_value, value))


def saturate(value):
    return clamp(value, 0.0, 1.0)


def hue_to_rgb(h):
    r = abs(h * 6.0 - 3.0) - 1.0
    g = 2.0 - abs(h * 6.0 - 2.0)
    b = 2.0 - abs(h * 6.0 - 4.0)
    return saturate(r), saturate(g), saturate(b)


def update_led(c):
    r, g, b = c
    led.fill((int(r * 255), int(g * 255), int(b * 255)))
    led.write()


led_pin = Pin(16, Pin.OUT)
led = NeoPixel(led_pin, 1)

color = 0

while color < 100:
    update_led(hue_to_rgb(color % 1))

    color = color + 0.005
    time.sleep_ms(10)

update_led((0, 0, 0))
