import tkinter as tk
from tkinter import ttk
from rpi_ws281x import Color
from led import Led  # Import your LED control class

import multiprocessing

class LedControlApp(tk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        self.configure(bg="white")
        self.master = master
        self.parent = parent
        
        self.led = Led(name="Ambient Light", LED_COUNT = 110)
        
        # Create GUI components
        self.create_widgets()
        self.led.color = Color(0, 0, 0)
        self.all_processes = []
        process = multiprocessing.Process(target = self.led.colorWipe())
        process.start()
        self.all_processes.append(process)
        

    def create_widgets(self):
        

        # Parent frame for RGB Sliders
        self.sliders_frame = tk.Frame(self, bg="white")
        self.sliders_frame.pack(pady=5)
        
        # Color Picker
        self.color_label = tk.Label(self.sliders_frame, text="Color Control", fg="black", bg="white", font=("Arial", 20))
        self.color_label.grid(row=0, column=1, padx=10)
        
        # RGB Sliders
        self.red_scale = self.create_color_slider(self.sliders_frame, "Red", 255,0)
        self.green_scale = self.create_color_slider(self.sliders_frame, "Green", 255,1)
        self.blue_scale = self.create_color_slider(self.sliders_frame, "Blue", 255,2)

        self.color_preview = tk.Label(self.sliders_frame, bg=self.rgb_to_hex(0, 0, 0), width=20, height=2)
        self.color_preview.grid(row=2,column=1,pady=5)

        # Apply Color Button
        self.color_button = tk.Button(self.sliders_frame, text="Apply Color", command=self.apply_color, bg="white", fg="black",font=("Arial", 18))
        self.color_button.grid(row=3, column=0, columnspan=3, pady=10)
    
        # Animation Controls
        self.animations = [
            ("Plain Color", self.led.colorWipe),
            ("Rainbow", self.led.rainbow),
            ("Rainbow Cycle", self.led.rainbowCycle),
            ("Flash", self.led.theaterChase),
            ("Flash Rainbow", self.led.theaterChaseRainbow)
        ]

        self.animation_label = tk.Label(self.sliders_frame, text="Select Animation:", fg="black", bg="white", font=("Arial", 20))
        self.animation_label.grid(row=0, column=3, padx=20,pady=10)

        self.animation_combobox = ttk.Combobox(self.sliders_frame, values=[a[0] for a in self.animations])
        self.animation_combobox.grid(row=1, column=3, padx=10, pady=2)

        self.start_animation_button = tk.Button(self.sliders_frame, text="Start Animation", command=self.start_animation, fg="black", bg="white",font=("Arial", 18))
        self.start_animation_button.grid(row=3, column=3, padx=50, pady=5)
    
        # Initial color update
        self.update_preview()
    
        self.back_button = tk.Button(self, text="Home page", command=self.go_back, fg="black", bg="white")
        self.back_button.pack(pady=10)


    def create_color_slider(self, parent, label_text, max_value,col):
        frame = tk.Frame(parent, bg="white")
        frame.grid(row=1,column=col,padx=5,pady=5)
    
        label = tk.Label(frame, text=label_text, fg="black", bg="white", font=("Arial", 18))
        label.pack()
    
        scale = tk.Scale(frame, from_=0, to=max_value, orient="vertical", command=self.update_preview)
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
    
    def go_back(self):
        self.grid_forget()  # Hide the current frame
        self.parent.show_main_frame()  # Show the main frame

