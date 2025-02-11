# main 主程序入口
import json
import tkinter as tk

import info
import frames
from leftmenu import LeftMenu


class Tools(tk.Tk):
    def __init__(self):
        super().__init__()
        self.left_menu_list = info.left_menu_list
        self.fc_list = info.fc_list

        self.cfg_path = 'cfg\\config.json'
        self.cfg = 'none'
        self.language = 'zh'
        self.text = {}  # 所有文本
        self.title("StarRailTools V0.1")
        self.geometry(f"800x600+100+100")
        self._load_cfg()  # 软件配置加载
        # self.save_cfg()  # 软件配置保存

        self.left_menu = LeftMenu(self, self.left_menu_list)  # 左侧栏
        self.current_frame = None
        self.frames = {}
        self._create_frames()  # 界面
        self.show_frame(self.fc_list[0])  # 初始界面

        self.character = info.CharacterInfo()  # 角色状态

    def _load_cfg(self):
        # load cfg
        with open(self.cfg_path, 'r') as file:
            self.cfg = json.load(file)

        # language text extraction
        self.language = self.cfg['language']
        path = f"cfg\\language\\{self.language}.json"
        with open(path, 'r') as file:
            self.text = json.load(file)
        # title
        self.title(self.cfg['title'])
        # geometry
        self.geometry(f"{self.cfg['width']}x{self.cfg['height']}+{self.cfg['x']}+{self.cfg['y']}")

    def save_cfg(self):
        pass

    def _create_frames(self):
        # 创建
        for frame_cls in self.fc_list:
            self.frames[frame_cls] = frame_cls(self)
            self.frames[frame_cls].pack_forget()  # 初始隐藏

    def show_frame(self, fc):  # fc: frame class
        if self.current_frame:
            self.current_frame.pack_forget()

        self.current_frame = self.frames[fc]
        self.current_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    tools = Tools()
    tools.mainloop()
