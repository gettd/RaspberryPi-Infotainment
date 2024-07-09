import tkinter as tk
from PIL import Image, ImageTk

class CarPlayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CarPlay Interface")
        self.geometry("800x480")
        self.configure(bg="white")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Grid frame
        grid_frame = tk.Frame(self, bg="white")
        grid_frame.pack(expand=True)
        
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
            button = self.create_app_button(grid_frame, app_name, icon_path)
            button.grid(row=row, column=col, padx=20, pady=20)
    
    def create_app_button(self, parent, app_name, icon_path):
        # Load and resize the icon
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((100, 100), Image.LANCZOS)
        icon = ImageTk.PhotoImage(icon_image)
        
        # Create a frame to hold the button and label
        frame = tk.Frame(parent, bg="white")
        
        # Create the button with the icon
        button = tk.Button(frame, image=icon, command=lambda: self.open_app(app_name), bg="white", relief="flat", bd=0, highlightthickness=0)
        button.image = icon  # Keep a reference to avoid garbage collection
        button.grid(row=0, column=0, padx=10, pady=10)
        
        # Create the app name label
        app_label = tk.Label(frame, text=app_name, fg="black", bg="white", font=("Arial", 12))
        app_label.grid(row=1, column=0)
        
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        return frame
    
    def open_app(self, app_name):
        print(f"Opening {app_name}...")

if __name__ == "__main__":
    app = CarPlayApp()
    app.mainloop()
