import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2

class CameraApp(tk.Frame):
    def __init__(self, master=None, parent=None):
        super().__init__(master)
        self.configure(bg="white")
        self.master = master
        self.parent = parent
        
        self.video_capture = cv2.VideoCapture(0)
        
        self.create_widgets()
        
    def create_widgets(self):
        self.video_label = tk.Label(self)
        self.video_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.back_button = tk.Button(self, text="Home page", command=self.go_back, fg="black", bg="white")
        self.back_button.grid(row=1, column=0, pady=10)
        
        self.update_video()
        
    def update_video(self):
        ret, frame = self.video_capture.read()
        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        self.after(10, self.update_video)
        
    def kill(self):
        self.video_capture.release()
        cv2.destroyAllWindows()
        
    def go_back(self):
        self.kill()
        self.grid_forget()  # Hide the current frame
        self.parent.show_main_frame()  # Show the main frame



