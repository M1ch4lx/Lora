import cv2
import os
import tkinter as tk
from PIL import Image, ImageTk

class LoraAnimationPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        # Create a frame for the listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create a scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox to display MP4 files
        self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        # Bind the listbox selection event
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Create a canvas to display the video frames
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack(side=tk.RIGHT)

        self.video_path = ""
        self.cap = None
        self.delay = 15  # Delay in ms between frames
        self.frame = None
        self.running = False

        # Dictionary to store filenames and their full paths
        self.file_paths = {}

        # Initial scan and populate MP4 files
        self.populate_file_list()

        # Periodically check for new files
        self.check_interval = 5000  # 5 seconds
        self.check_for_new_files()

    def populate_file_list(self):
        current_directory = os.getcwd()
        for root, dirs, files in os.walk(current_directory):
            # Exclude directories named 'partial_movie_files'
            dirs[:] = [d for d in dirs if d != 'partial_movie_files']
            for file in files:
                if file.endswith(".mp4"):
                    full_path = os.path.join(root, file)
                    filename = os.path.splitext(file)[0]  # Get filename without extension
                    if filename not in self.file_paths:
                        self.file_paths[filename] = full_path
                        self.listbox.insert(tk.END, filename)

    def check_for_new_files(self):
        new_files_found = False
        current_files = {}
        current_directory = os.getcwd()
        for root, dirs, files in os.walk(current_directory):
            # Exclude directories named 'partial_movie_files'
            dirs[:] = [d for d in dirs if d != 'partial_movie_files']
            for file in files:
                if file.endswith(".mp4"):
                    full_path = os.path.join(root, file)
                    filename = os.path.splitext(file)[0]  # Get filename without extension
                    current_files[filename] = full_path
                    if filename not in self.file_paths:
                        self.file_paths[filename] = full_path
                        self.listbox.insert(tk.END, filename)
                        new_files_found = True
        
        if new_files_found:
            print("New files added to the directory.")

        self.root.after(self.check_interval, self.check_for_new_files)

    def on_select(self, event):
        selected_idx = self.listbox.curselection()
        if selected_idx:
            selected_file = self.listbox.get(selected_idx)
            self.video_path = self.file_paths[selected_file]
            self.play_selected_video()

    def play_selected_video(self):
        if self.video_path:
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(self.video_path)
            self.running = True
            self.play_video()

    def play_video(self):
        if self.cap.isOpened() and self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.frame = ImageTk.PhotoImage(Image.fromarray(self.frame))
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frame)
                self.root.after(self.delay, self.play_video)
            else:
                self.cap.release()
                self.running = False

    def on_closing(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    player = LoraAnimationPlayer(root)
    root.protocol("WM_DELETE_WINDOW", player.on_closing)
    root.mainloop()
