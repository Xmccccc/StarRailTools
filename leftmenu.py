# import json
import tkinter as tk
# from tkinter import messagebox


class LeftMenu(tk.Frame):
    def __init__(self, parent, frames_dict):
        super().__init__(parent, width=150, bg='lightgray')
        self.pack(side='left', fill='y')

        self.parent = parent
        self.frames_dict = frames_dict

        # button
        for frame_name, frame_class in self.frames_dict.items():
            button = tk.Button(self, text=frame_class(self.parent).name,
                               command=lambda frame=frame_name: self.show_frame_callback(frame),
                               width=8, height=2,
                               font=('Georgia', 20))
            button.pack(pady=0, padx=0, fill='x')

    def show_frame_callback(self, frame_name):
        self.parent.show_frame(frame_name)
