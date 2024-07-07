#import RPi.GPIO as GPIO
class Door:
    def __init__(self, name, buttonpin):
        self.name = name
        self.buttonpin = buttonpin
        #GPIO.add_event_detect(self.buttonpin, GPIO.FALLING, callback=self.doorOpen_callback, bouncetime=200)

    def doorOpen_callback(channel):
        # write how to handle opening door here
        return 0
