# import json
import tkinter as tk


# from tkinter import messagebox


class LeftMenu(tk.Frame):
    def __init__(self, parent, frames_list):
        super().__init__(parent, width=150, bg='#2d2d2d')
        self.pack(side=tk.LEFT, fill=tk.Y)

        self.parent = parent
        self.frames_list = frames_list
        self.buttons = []

        # button
        for frame_cls in frames_list:
            btn = tk.Button(
                self,
                text=frame_cls(self.parent).name,
                command=lambda fc=frame_cls: self.show_frame_callback(fc),
                bg='#2d2d2d',  # 背景颜色
                fg='white',  # 文字颜色
                activebackground='#404040',  # 点击颜色
                anchor="center",  # 文字居中
                padx=20,
                pady=20,
                width=6,
                height=1,
                font=('微软雅黑', 20))  # 微软雅黑 Georgia
            btn.pack(fill=tk.X, padx=0, pady=0)
            # btn.pack(pady=0, padx=0, fill='x')
            self.buttons.append(btn)

    def show_frame_callback(self, fc):  # fc: frame class
        self.parent.show_frame(fc)
