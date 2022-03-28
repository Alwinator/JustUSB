# Programmed for Windows 10

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard, Keycode
from keyboard_layout_win_de import KeyboardLayout
from neopixel import NeoPixel

led = NeoPixel(board.GP16, 1)
led.fill((0, 0, 255))

try:
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayout(keyboard)

    time.sleep(2.5)
    led.fill((0, 255, 255))

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.3)

    keyboard_layout.write('cmd.exe /k "start https://www.youtube.com/watch?v=dQw4w9WgXcQ" && exit')
    keyboard.send(Keycode.ENTER)

    time.sleep(1.5)
    keyboard.send(Keycode.F11)

    keyboard.release_all()
    led.fill((0, 255, 0))
except Exception as ex:
    led.fill((255, 0, 0))
    keyboard.release_all()
    raise ex
