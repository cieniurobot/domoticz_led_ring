import argparse
import time
from neopixel import *


class LedRing():
    ''' Intelligent light '''
    # LED strip configuration:
    LED_COUNT = 16  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering
    LED_COLOR = Color(255, 0, 242)

    def __init__(self, color = Color(255, 0, 242)):
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT,
                                       self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL,
                                       self.LED_STRIP)
        self.strip.begin()
        self.led_color = color

    def off(self, wait_ms=50):
        for i in range(self.strip.numPixels()):
            color = Color(0, 0, 0)
            self.strip.setPixelColor(i, color)
            self.strip.show()
            print("turn_led_off i: {0}".format(i))
            time.sleep(wait_ms / 1000.0)

    def on(self, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.led_color)
            self.strip.show()
            print("turn_led_on i: {0}".format(i))
            time.sleep(wait_ms / 1000.0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Turn led ring on/off.')
    parser.add_argument('state', metavar='state', type=int, nargs='+',
                        help='1 - turn on, 0 - turn off')
    parser.add_argument('--color', help='Set LED RGB color string. Example: 255,0,255')
    args = parser.parse_args()
    led_state = False

    if args.state[0] == 1:
        print("Turn on")
        led_state = True
    else:
        print("Turn off")
        led_state = False

    if args.color is not None:
        color = Color(args.color)
        led_ring = LedRing(color)
    else:
        led_ring = LedRing()

    if led_state:
        led_ring.on()
    else:
        led_ring.off()

