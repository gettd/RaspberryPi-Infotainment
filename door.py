import RPi.GPIO as GPIO
import time
from threading import *

class Door(Thread):
    def set(self, name, sensor_pin, led_pin):
        self.name = name
        self.sensor_pin = sensor_pin
        self.led_pin = led_pin

    def door_close_callback(self, channel):
        if not GPIO.input(self.sensor_pin):  # Door opened
            print(f"{self.name} - Door close!")
            self.handle_door_close()

    def handle_door_close(self):
        print(f"Handling {self.name} door close event.")
        # Add code to handle door open event (Update the touchscreen display)
        

    def cleanup(self):
        GPIO.remove_event_detect(self.sensor_pin)
        GPIO.cleanup()
        
    def run(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.led_pin, GPIO.OUT)
        
        #GPIO.add_event_detect(self.sensor_pin, GPIO.FALLING, callback=self.door_close_callback, bouncetime=200)
        
        #print(f"Door sensor initialized for {self.name}. GPIO pin: {self.sensor_pin}")
        while True:
            if not GPIO.input(self.sensor_pin):
                #print('Door Close')
                GPIO.output(self.led_pin,GPIO.LOW)
            else:
                #print('Door open')
                GPIO.output(self.led_pin,GPIO.HIGH)
                
            #time.sleep(1)

# Example usage:
'''
if __name__ == "__main__":
    door1 = Door("Car Door", 17)  # Replace 3 with actual GPIO pin
    
    try:
        # Keep the main thread alive to wait for interrupts
        while True:
            if GPIO.input(17):
                print('Door open')
            time.sleep(1)
    except KeyboardInterrupt:
        door1.cleanup()
'''
