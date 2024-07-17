import tkinter as tk
import folium
import os
import webview
from webview import create_window, start
from geopy.geocoders import Nominatim
import requests
import threading

class MapApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Map App")
        self.geometry("800x480")
        self.configure(bg="black")
        
        self.create_map()
        self.create_browser()
    
    def get_approximate_location(self):
        try:
            response = requests.get('https://ipinfo.io/')
            data = response.json()
            location = data['loc'].split(',')
            return float(location[0]), float(location[1])
        except:
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode("Bangkok")
            return location.latitude, location.longitude

    def create_map(self):
        latitude, longitude = self.get_approximate_location()
        
        m = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker([latitude, longitude], tooltip='Bangkok').add_to(m)
        
        map_file = "map.html"
        m.save(map_file)
        self.map_file = os.path.abspath(map_file)
    
    def create_browser(self):
        # Create a frame for the browser
        self.browser_frame = tk.Frame(self, bg="black")
        self.browser_frame.pack(fill="both", expand=True)
        
        # Start PyWebview
        threading.Thread(target=self.start_webview).start()
    
    def start_webview(self):
        window = create_window("Map", self.map_file, width=800, height=480)
        start()

if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(master=root)
    root.mainloop()
