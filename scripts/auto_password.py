# Automatically enters the password after Macbook Pro boot (US layout)

import time
import math
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard, Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from neopixel import NeoPixel

led = NeoPixel(board.GP16, 1)


# basically time.sleep, but with a LED animation
def wait_animation(secs: float, animation_interval: float = 0.01):
    time_running = 0
    while time_running < secs:
        animation_progress = time_running / secs
        print(animation_progress)
        multiplier = math.sin(animation_progress * math.pi * int(secs))
        led.fill((0, multiplier * 255, 255))
        time.sleep(animation_interval)
        time_running += animation_interval


try:
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)

    wait_animation(7.5)

    keyboard_layout.write('mySuper!SecretPassword123%%%')
    time.sleep(0.1)
    keyboard.send(Keycode.ENTER)

    keyboard.release_all()

    for _ in range(3):
        time.sleep(0.1)
        led.fill((0, 255, 0))
        time.sleep(0.1)
        led.fill((0, 0, 0))

except Exception as ex:
    led.fill((255, 0, 0))
    keyboard.release_all()
    raise ex
