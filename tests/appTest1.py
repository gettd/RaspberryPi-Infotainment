import tkinter as tk
from tkinter import ttk

class InfotainmentApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Car Infotainment System")
		self.geometry("1024x600")
		self.create_widgets()

	def create_widgets(self):
		nav_frame = tk.Frame(self)
		nav_frame.pack(side="top", fill="x")

		home_button = tk.Button(nav_frame, text="Home", command=self.show_home)
		home_button.pack(side="left", fill="x", expand=True)

		nav_button = tk.Button(nav_frame, text="Navigation", command=self.show_navigation)
		nav_button.pack(side="left", fill="x", expand=True)

		light_button = tk.Button(nav_frame, text="Light",command=self.show_light)
		light_button.pack(side="left", fill="x", expand=True)

		settings_button = tk.Button(nav_frame, text="Settings", command=self.show_settings)
		settings_button.pack(side="left", fill="x", expand=True)

		self.home_frame = tk.Frame(self, bg="lightblue")
		self.nav_frame = tk.Frame(self, bg="lightgreen")
		self.light_frame = tk.Frame(self, bg="pink")
		self.settings_frame = tk.Frame(self, bg="lightyellow")

		home_label = tk.Label(self.home_frame, text="Home page", font=("Arial", 20))
		home_label.pack(pady=20)
		nav_label = tk.Label(self.nav_frame, text="Navigation", font=("Arial", 20))
		nav_label.pack(pady=20)
		light_label = tk.Label(self.light_frame, text="Light control", font=("Arial",20))
		light_label.pack(pady=20)
		settings_label = tk.Label(self.settings_frame, text="Settings", font=("Arial", 20))
		settings_label.pack(pady=20)

		self.show_home()

	def show_home(self):
		self.home_frame.pack(fill="both", expand=True)
		self.nav_frame.pack_forget()
		self.light_frame.pack_forget()
		self.settings_frame.pack_forget()

	def show_navigation(self):
		self.home_frame.pack_forget()
		self.nav_frame.pack(fill="both", expand=True)
		self.light_frame.pack_forget()
		self.settings_frame.pack_forget()

	def show_light(self):
		self.home_frame.pack_forget()
		self.nav_frame.pack_forget()
		self.light_frame.pack(fill="both",expand=True)
		self.settings_frame.pack_forget()

	def show_settings(self):
		self.home_frame.pack_forget()
		self.nav_frame.pack_forget()
		self.light_frame.pack_forget()
		self.settings_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
	app = InfotainmentApp()
	app.mainloop()

