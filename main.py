# main 主程序入口
# import json
import tkinter as tk

from leftmenu import LeftMenu
import frames


class Tools(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("StarRailTools V0.1")

        self.position = 'none'  # 当前位置
        self.energy = 0  # 能量、体力
        self.stored_energy = 0  # 储存能量、储存体力
        self.money = 0  # 钱、金币

        self.set_windows_position()  # 窗口
        self.left_button_dict = frames.left_button_dict
        self.frames_dict = frames.frames_dict
        self.frames = {}
        self.create_frames()  # 界面
        LeftMenu(self, self.left_button_dict)  # 左侧栏

    def set_windows_position(self):
        # 获取屏幕尺寸
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # 设置窗口大小为屏幕的70%（可根据需求调整比例）
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)

        # 计算居中坐标
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2 - 30

        # 设置窗口位置和尺寸
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_frames(self):
        # 创建
        for frame_name, frame_class in self.frames_dict.items():
            self.frames[frame_name] = frame_class(self)
        # 显示
        self.frames['FrameTools'].pack(side='right', fill='both', expand=True)

    def show_frame(self, frame_name):
        # 隐藏
        for frame in self.frames.values():
            frame.pack_forget()
        # 显示
        self.frames[frame_name].pack(side='right', fill='both', expand=True)


if __name__ == "__main__":
    tools = Tools()
    tools.mainloop()
