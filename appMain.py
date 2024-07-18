import tkinter as tk
from door import Door
from PIL import Image, ImageTk
from ledControl import LedControlApp

class CarPlayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CarPlay Interface")
        #self.geometry("800x480")
        self.geometry("1024x600")
        self.configure(bg="white")
        
        self.grid_frame= tk.Frame(self,bg="white")
        self.grid_frame.grid(row=0, column=0, sticky="nsew")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #self.content_frames ={}
        self.create_widgets()
    
    def create_widgets(self):
        # Grid frame
        self.grid_frame = tk.Frame(self, bg="white")
        self.grid_frame.grid(row=0,column=0)
        
        # List of apps
        apps = [
            ("Media", "/home/egco/Desktop/InfotainmentApp/Icon/music.png"),
            ("Navigation", "/home/egco/Desktop/InfotainmentApp/Icon/maps.png"),
            ("Rear Camera", "/home/egco/Desktop/InfotainmentApp/Icon/camera.png"),
            ("Browser", "/home/egco/Desktop/InfotainmentApp/Icon/safari.png"),
            ("Ambient Light", "/home/egco/Desktop/InfotainmentApp/Icon/game-center.png"),
            ("Settings", "/home/egco/Desktop/InfotainmentApp/Icon/settings.png"),
        ]
        
        # Create buttons for each app
        for i, (app_name, icon_path) in enumerate(apps):
            row = i // 3
            col = i % 3
            button = self.create_app_button(self.grid_frame, app_name, icon_path)
            button.grid(row=row, column=col, padx=50, pady=50)
            
       
    
    def create_app_button(self, parent, app_name, icon_path):                                  
        # Load and resize the icon
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((130, 130), Image.LANCZOS)
        icon = ImageTk.PhotoImage(icon_image)
        
        # Create a frame to hold the button and label
        frame = tk.Frame(parent, bg="white")
        
        # Create the button with the icon
        button = tk.Button(frame, image=icon, command=lambda: self.open_app(app_name), bg="white", relief="flat", bd=0, highlightthickness=0)
        button.image = icon  # Keep a reference to avoid garbage collection
        button.grid(row=0, column=0, padx=50, pady=0)
        
        # Create the app name label
        app_label = tk.Label(frame, text=app_name, fg="black", bg="white", font=("Arial", 16))
        app_label.grid(row=1, column=0)
        
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        return frame
    
    def open_app(self, app_name):
        print(f"Opening {app_name}...")
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        if app_name == "Ambient Light":
            LedControlApp(self.grid_frame, parent=self).grid(row=0, column=0, sticky="nsew")
    
    
    def show_main_frame(self):
        self.grid_frame.grid(row=0, column=0, sticky="nsew")
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.create_widgets()
    

if __name__ == "__main__":
    door1 = Door()
    door1.set(name = "Car Door", sensor_pin = 17, led_pin = 13)
    door1.start()
    app = CarPlayApp()
    app.mainloop()


