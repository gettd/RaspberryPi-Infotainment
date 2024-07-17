import RPi.GPIO as GPIO
import time

class Door:
    def __init__(self, name, sensor_pin):
        self.name = name
        self.sensor_pin = sensor_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.add_event_detect(self.sensor_pin, GPIO.FALLING, callback=self.door_open_callback, bouncetime=200)
        
        print(f"Door sensor initialized for {self.name}. GPIO pin: {self.sensor_pin}")

    def door_open_callback(self, channel):
        if not GPIO.input(self.sensor_pin):  # Door opened
            print(f"{self.name} - Door opened!")
            self.handle_door_open()

    def handle_door_open(self):
        print(f"Handling {self.name} door open event.")
        # Add code to handle door open event (Update the touchscreen display)

    def cleanup(self):
        GPIO.remove_event_detect(self.sensor_pin)
        GPIO.cleanup()

# Example usage:
"""
if __name__ == "__main__":
    door1 = Door("Car Door", 3)  # Replace 3 with actual GPIO pin
    
    try:
        # Keep the main thread alive to wait for interrupts
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        door1.cleanup()
"""
