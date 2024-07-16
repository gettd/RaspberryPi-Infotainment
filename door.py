import RPi.GPIO as GPIO
import time

class Door:
    def __init__(self, name, sensor_pin): 
        self.name = name 
        self.sensor_pin = sensor_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.sensor_pin, GPIO.BOTH, callback=self.door_event_callback, bouncetime=200)
        
        print(f"Door sensor initialized for {self.name}.")

    def door_event_callback(self, channel):
        if GPIO.input(self.sensor_pin):  
            print(f"{self.name} - Door closed.")
            # Add code to handle door closed event
        else:  
            print(f"{self.name} - Door opened!")
            # Add code to handle door opened event

    def cleanup(self):
        GPIO.remove_event_detect(self.sensor_pin)
        GPIO.cleanup()


# Example usage:
"""
if __name__ == "__main__":
    # Instantiate multiple instances of Door
    door1 = Door("Car Door 1", 17)  # Replace 17 with GPIO pin for first door
    door2 = Door("Car Door 2", 18)  # Replace 18 with GPIO pin for second door
    door3 = Door("Car Door 3", 19)  # Replace 19 with GPIO pin for third door
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        door1.cleanup()
        door2.cleanup()
        door3.cleanup()
"""
