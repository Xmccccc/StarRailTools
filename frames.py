import os
import time
import json
import tkinter as tk
from tkinter import ttk

import utils


class FrameBase(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.text = self.parent.text
        self.name = 'none'  # 进入此界面的按钮文本

        self.font = self.parent.cfg["font"]
        self.font_size = self.parent.cfg["font_size"]

    def show_frame_callback(self, fc):  # fc: frame class
        self.parent.show_frame(fc)


class FrameTools(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["function"]  # 进入此界面的按钮文本
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


class FrameTheme(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["theme"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="主题")
        button01.pack()


class FrameSetting(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["settings"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="设置")
        button01.pack()


class FrameAbout(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["about"]  # 进入此界面的按钮文本

        # button
        button01 = tk.Button(self, text="关于")
        button01.pack()


class FrameDig(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["dig"]  # 锄地
        self.dig_maps = []
        self.select_maps = []
        # self.parent.intf_mgr.maps

        # label
        tk.Label(self, text=self.text['map_choice'], font=(self.font, self.font_size)).pack(side=tk.LEFT)

        # treeview
        tree = ttk.Treeview(
            self.parent,
            columns='selected',
            show="tree headings",
            selectmode="none"
        )

        # button
        tk.Button(self, text=self.text['start'], command=self.parent.launch_scripts(None, self.dig()), ).pack(side=tk.LEFT)

    def dig(self):
        pass


class FrameStory(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["story"]  # 剧情

        # button info

        tk.Button(self, text=self.name, command=lambda: print(self.name),
                  width=8, height=1, font=('Georgia', 14)).grid()


class FrameSimulatedUniverse(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["simulated_universe"]  # 模拟宇宙

        # button info

        # button
        button01 = tk.Button(self, text="模拟宇宙")
        button01.pack()


class FrameForgottenHall(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["forgotten_hall"]  # 忘却之庭

        # button info

        # button
        button01 = tk.Button(self, text="忘却之庭")
        button01.pack()


class FrameRunningInfo(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["running_info"]

        self.task = {}  # 任务列表
        self.labels = []  # 运行信息显示
        self.run_info = []
        self.info_num = self.parent.cfg["info_num"]
        for i in range(self.info_num):
            label = tk.Label(
                self,
                text=f"text_{i}"

            )
            label.pack()
            self.run_info.append(label.cget('text'))
            self.labels.append(label)

    def minimize_launch(self):
        while not self.parent.character.running:
            self.parent.character.running = utils.is_program_running(self.text['exe_name'])
            if self.parent.character.running:
                self.save_log(self.text['running'])
            else:
                self.save_log(self.text['no_running'])
                utils.launch_program(self.text['paths']['exe'])
                time.sleep(8)
        self.save_log(self.text['launch_S'])

        while not self.parent.character.minimize:
            self.save_log(self.text['minimize_S'])
            self.parent.character.minimize = utils.minimize_window(self.text['exe_name'])
        self.save_log(self.text['minimize_S'])

    def save_log(self, text):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        text = f"[{current_time}]\t{text}"

        utils.text_save(f'logs\\{self.parent.log_file_name}.txt', text)
        self.renew_info(text)

    def renew_info(self, text):
        self.run_info.append(text)
        self.run_info.pop(0)
        for i in range(self.info_num):
            self.labels[i].config(text=self.run_info[i])

    # def backend_launch(program_exe, exe_path, window_title):
    #     running = game_utils.is_program_running(program_exe)
    #     if not running:
    #         game_utils.launch_program(exe_path)
    #         running = game_utils.is_program_running(program_exe)
