import os
import json
import tkinter as tk


class FrameBase(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = 'none'  # 进入此界面的按钮文本

        self.font = self.parent.cfg["font"]
        self.font_size = self.parent.cfg["font_size"]

    def show_frame_callback(self, fc):  # fc: frame class
        self.parent.show_frame(fc)


class FrameTools(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["function"]  # 进入此界面的按钮文本
        self.buttons = []

        # button info
        buttons_info = [
            (FrameDig, 0, 0),
            (FrameStory, 0, 1),
            (FrameSimulatedUniverse, 0, 2),
            (FrameForgottenHall, 0, 3),
            (FrameDig, 1, 0),
            (FrameDig, 1, 1),
        ]

        # button
        for frame_cls, row, col in buttons_info:  # fc: frame class
            btn = tk.Button(
                self,
                text=frame_cls(parent).name,
                command=lambda fc=frame_cls: self.show_frame_callback(fc),
                # bg='#2d2d2d',
                # fg='white',
                # activebackground='#404040',
                # padx=8,
                # pady=6,
                width=8,
                height=1,
                font=(self.font, self.font_size))  # 微软雅黑  Georgia  14
            btn.grid(row=row, column=col, padx=20, pady=20)
            self.buttons.append(btn)

        # label
        # label01 = tk.Label(self, text="功能界面", font=('Georgia', 14))
        # label01.grid()


class FrameTheme(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["theme"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="主题")
        button01.pack()

        # label
        label01 = tk.Label(self, text="主题界面")
        label01.pack()


class FrameSetting(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["settings"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="设置")
        button01.pack()

        # label
        label01 = tk.Label(self, text="设置界面")
        label01.pack()


class FrameAbout(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["about"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="关于")
        button01.pack()

        # label
        label01 = tk.Label(self, text="关于界面")
        label01.pack()


class FrameDig(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["dig"]  # 锄地

        # label
        tk.Label(self, text="地图选择", font=('Georgia', 14)).grid(row=0, column=0, padx=20, pady=10)
        # button
        tk.Button(self, text="锄地").grid(row=1, column=0, padx=20, pady=10)


class FrameStory(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["story"]  # 剧情

        # button info

        tk.Button(self, text=self.name, command=lambda: print(self.name),
                  width=8, height=1, font=('Georgia', 14)).grid()


class FrameSimulatedUniverse(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["simulated_universe"]  # 模拟宇宙

        # button info

        tk.Button(self, text=self.name, command=lambda: print(self.name),
                  width=8, height=1, font=('Georgia', 14)).grid()


class FrameForgottenHall(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.parent.text["forgotten_hall"]  # 忘却之庭

        # button info

        tk.Button(self, text=self.name, command=lambda: print(self.name),
                  width=8, height=1, font=('Georgia', 14)).grid()
