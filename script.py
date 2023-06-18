import cv2
import numpy as np
import pyautogui
import tkinter as tk
import threading

class ScreenRecorder:
    def __init__(self):
        self.recording = False
        self.resolution = (1920, 1080)
        self.fps = 15
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.video_output = None
    
    def start_recording(self):
        self.recording = True
        self.video_output = cv2.VideoWriter("record.avi", self.codec, self.fps, self.resolution)
        
        while self.recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.video_output.write(frame)
            
        self.video_output.release()
        
    def stop_recording(self):
        self.recording = False

recorder = ScreenRecorder()

def start_recording():
    start_button["state"] = tk.DISABLED
    stop_button["state"] = tk.NORMAL
    recording_thread = threading.Thread(target=recorder.start_recording)
    recording_thread.start()

def stop_recording():
    start_button["state"] = tk.NORMAL
    stop_button["state"] = tk.DISABLED
    recorder.stop_recording()

# Create the tkinter window
window = tk.Tk()
window.title("ScRecor")
window.iconbitmap("iconFilm.ico")
window.configure(bg="#189100")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate window position
x_coordinate = int((screen_width / 2) - (window.winfo_reqwidth() / 2))
y_coordinate = int((screen_height / 2) - (window.winfo_reqheight() / 2))

# Center the window on the screen
window.geometry(f"+{x_coordinate}+{y_coordinate}")

# Make the window unresizable
window.resizable(False, False)

# Create the "Start Recording" button
start_button = tk.Button(window, text="Start Recording", command=start_recording)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the "Stop Recording" button
stop_button = tk.Button(window, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the tkinter event loop
window.mainloop()