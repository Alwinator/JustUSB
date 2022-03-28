![header image](./images/top.jpg)
# Just USB
A custom-built USB stick which registers as HID-keyboard to automatically run commands.

## Assebmly
![assembly image](./images/assembly.jpg)

You can find the 3D model on [thingiverse](https://www.thingiverse.com/thing:5332207). After printing simply put the electronics inside the case and stick everything together.

### Price

| Name                                                                 | Amazon DE Price (Price I paid)  | AliExpress Price (longer delivery)  |
|----------------------------------------------------------------------|-----------------|--------------------------------------|
| [Waveshare RP2040-Zero](https://www.waveshare.com/wiki/RP2040-Zero) | [11.95€](https://www.amazon.de/gp/product/B09M42BS6H)          | [6.52€ ($6.98)](https://www.aliexpress.com/item/1005003813286792.html)|
| USB to USB C Adapter  |  [9.56€](https://www.amazon.de/gp/product/B09L4GXQZX)          | [0.66€ ($0.60)](https://www.aliexpress.com/item/1005002069300990.html)|
| [3D Printed Case](https://www.thingiverse.com/thing:5332207)         | ~0.25€          | ~0.25€ (0.27$) |
| Total                                                                | 21.76€          | 7.43€  (7.85$) |

Austrian Prices, prices in other countries are usually cheaper

## Setup
1. Install CircitPython as described [here](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython).
2. I recommend PyCharm for programming, to upload scripts simply move them to the drive of the microcontroller
3. Show terminal using `sudo chmod 777 /dev/ttyACM0` and `screen /dev/ttyACM0 115200` (on Ubuntu)
4. Upload [setup.py](scripts/setup.py) and run it once, then overwrite it with [rick_roll.py](scripts/rick_roll.py) or [keyboard.py](scripts/keyboard.py)
5. Done! Happy Hacking!

## Disclaimer
This project is for educational use only. I assume no liability for software or hacking damage.
