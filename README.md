![header image](./images/top.jpg)
# Just USB
A custom-built USB stick which registers as an HID keyboard to automatically run commands.

[![CircuitPython](https://img.shields.io/static/v1?label=Programming%20Language&message=CircuitPython&color=%23652d90&style=flat-square)](https://circuitpython.org/)
[![Thingiverse](https://img.shields.io/static/v1?label=3D%20Model&message=Thingiverse&color=%230359b5&style=flat-square)](https://www.thingiverse.com/thing:5332207)
[![License](https://img.shields.io/github/license/Alwinator/JustUSB?color=%23009900&style=flat-square)](https://github.com/Alwinator/JustUSB/blob/main/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/Alwinator/JustUSB?style=flat-square)](https://github.com/Alwinator/JustUSB)



![presentation](./images/presentation.gif)

## Assembly
![assembly image](./images/assembly.jpg)

You can find the 3D model on [thingiverse](https://www.thingiverse.com/thing:5332207). After printing, simply put the electronics inside the case and snap the parts together.

### Price

| Name                                                                | Amazon DE Price (Price I paid)                        | AliExpress Price (longer delivery)                                     |
|---------------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------|
| [Waveshare RP2040-Zero](https://www.waveshare.com/wiki/RP2040-Zero) | [€11.95](https://www.amazon.de/gp/product/B09M42BS6H) | [€6.52 ($6.98)](https://www.aliexpress.com/item/1005003813286792.html) |
| USB to USB C Adapter                                                | [€9.56](https://www.amazon.de/gp/product/B09L4GXQZX)  | [€0.66 ($0.60)](https://www.aliexpress.com/item/1005002069300990.html) |
| [3D Printed Case](https://www.thingiverse.com/thing:5332207)        | ~€0.25                                                | ~€0.25 ($0.27)                                                         |
| Total                                                               | €21.76                                                | €7.43  ($7.85)                                                         |

Austrian Prices listed, prices in other countries are usually less

## Setup
1. Install CircitPython as described [here](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython).
2. I recommend PyCharm for programming. To upload scripts, simply move them to the drive of the microcontroller.
3. Show terminal using `sudo chmod 777 /dev/ttyACM0` and `screen /dev/ttyACM0 115200` (on Ubuntu)
4. Upload [setup.py](scripts/setup.py) and run it once, then overwrite it with [rick_roll.py](scripts/rick_roll.py)
5. Done! Happy Hacking!

## Disclaimer
This project is for educational purposes only. I assume no liability for software or hacking damage.
