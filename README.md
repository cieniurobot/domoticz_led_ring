# domoticz_led_ring

Domoticz switch script for led ring.

**Required neopixel library!**

## Installation
Neopixel installation instruction is here  [https://learn.adafruit.com/neopixels-on-raspberry-pi/software](https://learn.adafruit.com/neopixels-on-raspberry-pi/software)
Clone repository:

    cd domoticz/scripts/python
    git clone https://github.com/cieniurobot/domoticz_led_ring
    cd domoticz_led_ring
    chmod +x led_ring.py

## Usage: 
Turn on: `python led_ring.py 1` or with optional color `python led_ring.py 1 --color 255,0,255`
Turn off: `python led_ring.py 0`
