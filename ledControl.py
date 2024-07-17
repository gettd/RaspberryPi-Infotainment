import tkinter as tk
from tkinter import ttk
from rpi_ws281x import Color
from led import Led  # Import your LED control class

import multiprocessing

class LedControlApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.title("LED Control")
        #self.geometry("800x480")
        #self.configure(bg="black")
        
        self.led = Led(name="Ambient Light")
        
        # Create GUI components
        self.create_widgets()
        self.led.color = Color(0, 0, 0)
        self.all_processes = []
        process = multiprocessing.Process(target = self.led.colorWipe())
        process.start()
        self.all_processes.append(process)
        

    def create_widgets(self):
        # Color Picker
        self.color_label = tk.Label(self, text="Select Color:", fg="white", bg="black", font=("Arial", 14))
        self.color_label.pack(pady=10)

        # RGB Sliders
        self.red_scale = self.create_color_slider("Red", 255)
        self.green_scale = self.create_color_slider("Green", 255)
        self.blue_scale = self.create_color_slider("Blue", 255)
        
        self.color_preview = tk.Label(self, bg=self.rgb_to_hex(0, 0, 0), width=20, height=2)
        self.color_preview.pack(pady=10)
        
        self.color_button = tk.Button(self, text="Apply Color", command=self.apply_color, bg="black", fg="white")
        self.color_button.pack(pady=10)
        
        # Animation Controls
        self.animations = [
            ("Plain Color", self.led.colorWipe),
            ("Rainbow", self.led.rainbow),
            ("Rainbow Cycle", self.led.rainbowCycle),
            ("Flash", self.led.theaterChase),
            ("Flash Rainbow", self.led.theaterChaseRainbow)
        ]
        
        self.animation_label = tk.Label(self, text="Select Animation:", fg="white", bg="black", font=("Arial", 14))
        self.animation_label.pack(pady=10)
        
        self.animation_combobox = ttk.Combobox(self, values=[a[0] for a in self.animations])
        self.animation_combobox.pack(pady=10)
        
        self.start_animation_button = tk.Button(self, text="Start Animation", command=self.start_animation, bg="black", fg="white")
        self.start_animation_button.pack(pady=10)
        
        # Initial color update
        self.update_preview()

    def create_color_slider(self, label_text, max_value):
        frame = tk.Frame(self, bg="black")
        frame.pack(pady=5)
        
        label = tk.Label(frame, text=label_text, fg="white", bg="black", font=("Arial", 12))
        label.pack()
        
        scale = tk.Scale(frame, from_=0, to=max_value, orient="horizontal", command=self.update_preview)
        scale.pack()
        scale.set(max_value)  # Default to max value
        
        return scale
    
    def update_preview(self, _=None):
        red = self.red_scale.get()
        green = self.green_scale.get()
        blue = self.blue_scale.get()
        hex_color = self.rgb_to_hex(red, green, blue)
        self.color_preview.config(bg=hex_color)

    def apply_color(self):
        red = self.red_scale.get()
        green = self.green_scale.get()
        blue = self.blue_scale.get()
        #color = Color(int(red), int(green), int(blue))
        #self.led.colorWipe(color)
        self.led.color = Color(int(red), int(green), int(blue))
        #self.running_animation = threading.Thread(target = self.led.colorWipe())
        self.led.colorWipe()
    
    def start_animation(self):
        for process in self.all_processes:
            process.terminate()
        animation_name = self.animation_combobox.get()
        for name, func in self.animations:
            if name == animation_name:
                process = multiprocessing.Process(target = func)
                #func()
                process.start()
                self.all_processes.append(process)
                break
        
    
    def rgb_to_hex(self, r, g, b):
        return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

'''
if __name__ == "__main__":
    root = tk.Tk()
    app = LedControlApp(master=root)
    root.mainloop()
'''
