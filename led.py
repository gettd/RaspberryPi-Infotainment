from rpi_ws281x import *
import argparse
import time


class Led:
    def __init__(self, name, LED_COUNT=30, LED_PIN=18, LED_FREQ_HZ=800000, LED_DMA=10, LED_BRIGHTNESS=65,
                 LED_INVERT=False, LED_CHANNEL=0):
        # PWM0_0 available on GPIO 12, 18 or 52.
        # PWM0_1 available on GPIO 13, 19, 45 or 53
        self.name = name
        self.LED_COUNT = LED_COUNT  # Number of LED pixels.
        self.LED_PIN = LED_PIN  # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = LED_FREQ_HZ  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = LED_DMA  # DMA channel to use for generating a signal (try 10)
        self.LED_BRIGHTNESS = LED_BRIGHTNESS  # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = LED_INVERT  # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL = LED_CHANNEL  # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,
                                       LED_CHANNEL)
        self.strip.begin()

    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, color)
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)

    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((i + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, self.wheel((i + j) % 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)
