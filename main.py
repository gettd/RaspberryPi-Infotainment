import door
import led #uncomment when ready and installed all required packages
import camera
from rpi_ws281x import *
import argparse
import time


def main():
    # where all the main stuff goes
    # make all display features in main

    # example of creating and calling a constructor
    #door1 = door.Door(name='door1', buttonpin=3)
    #print(door1.name)
    #

    #Checking if main was called
    #print(0)
    test = led.Led('test', LED_COUNT=4)
    while True:
        test.colorWipe(Color(0,0,0))
        #test.rainbow()
        #test.theaterChase(Color(127,127,127))
    return 0


if __name__ == "__main__":
    main()
