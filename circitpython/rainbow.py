import time
import board
import neopixel
import colorsys

pixels = neopixel.NeoPixel(board.GP16, 1)
color = 0

while True:
    pixels.fill(colorsys.hls_to_rgb(color % 1, 0.5, 1))
    color += 0.01
    time.sleep(0.1)
