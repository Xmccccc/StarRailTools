# main 主程序入口
import os
import time
import tkinter as tk

import frames
import info
import utils
from leftmenu import LeftMenu


class Tools(tk.Tk):
    def __init__(self):
        super().__init__()
        self.left_menu_list = info.left_menu_list
        self.fc_list = info.fc_list

        self.cfg_path = 'cfg\\config.json'
        self.log_file_name = time.strftime("%Y_%m_%d_%H_%M", time.localtime())

        self._load_cfg()  # 软件配置加载
        utils.text_save(f'logs\\{self.log_file_name}.txt', '程序启动')

        self.intf_mgr = info.InterfaceManage(self)  # 游戏界面管理类
        self.intf_mgr.load_maps()
        self.character = info.Character()  # 角色状态

        self.left_menu = LeftMenu(self, self.left_menu_list)  # 左侧栏
        self.current_frame = None
        self.frames = {}
        self._create_frames()  # 界面
        self.show_frame(self.fc_list[0])  # 初始界面

        # self.save_cfg()  # 软件配置保存

    def _load_cfg(self):
        # cfg  配置参数等
        self.cfg = utils.load_json_file(self.cfg_path)

        # language  语言类型
        self.language = self.cfg['language']
        # text  所有文本
        self.text = utils.load_json_file(self.cfg['paths'][self.language])
        # title  标题
        self.title(self.cfg['title'])
        # geometry  窗口大小
        self.geometry(f"{self.cfg['width']}x{self.cfg['height']}+{self.cfg['x']}+{self.cfg['y']}")
        # resizable
        self.resizable(width=self.cfg['resizable_w'], height=self.cfg['resizable_h'])
        # ico
        self.iconbitmap(self.cfg['paths']['ico'])

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

    def check_cfg(self):
        # 游戏路径检测
        pass

    def launch_scripts(self, task, scripts):
        # self.show_frame(frames.FrameRunningInfo)
        # self.current_frame.minimize_launch()
        # for script in scripts:
        #     script()
        pass


def end_sign():
    pass


if __name__ == "__main__":
    # utils.require_admin()
    tools = Tools()
    tools.mainloop()
