# main 主程序入口
import os
import time
import tkinter as tk

import frames
import tools
import utils
from leftmenu import LeftMenu
import threading


class Tools(tk.Tk):
    def __init__(self):
        super().__init__()
        self.left_menu_list = tools.left_menu_list
        self.fc_list = tools.fc_list

        self.cfg_path = 'cfg\\config.json'
        self._load_cfg()  # 软件配置加载

        self.log_file_name = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
        self.log_path = f"logs\\{self.log_file_name}.txt"
        self.log_info_num = self.cfg['log_info_num']  # 消息显示数量
        utils.text_save_to_file(self.log_path, '工具启动')

        self.info_show = utils.InfoShow(self)  # 显示空心框和信息

        self.intf_mgr = tools.IntfManage(self)  # 游戏界面管理类
        self.intf_mgr.load_intf()

        self.left_menu = LeftMenu(self, self.left_menu_list)  # 左侧栏
        self.current_frame = None
        self.frames = {}
        self._create_frames()  # 界面
        self.show_frame(self.fc_list[0])  # 初始界面

        self.character = tools.Character(self)
        self.task_list = []  # 将要执行的任务  dig、...
        self.task_info = utils.load_json_file(r'user_cfg\task\task.json')  # 任务信息

        # self.save_cfg()  # 软件配置保存

    def _load_cfg(self):
        # cfg  配置参数等
        self.cfg = utils.load_json_file(self.cfg_path)

        # ico 窗口图标
        self.iconbitmap(self.cfg['paths']['ico'])
        # language  语言类型
        self.language = self.cfg['language']
        # text  所有文本
        self.text = utils.load_json_file(self.cfg['paths'][self.language])
        # intf 界面信息 - 界面、界面元素-按钮、按键
        self.intf_info = utils.load_json_file(self.cfg['paths']['intf'])
        self.intf_element_info = utils.load_json_file(self.cfg['paths']['intf_element'])
        # title  标题
        self.title(self.cfg['title'])
        # geometry  窗口大小
        self.geometry(f"{self.cfg['width']}x{self.cfg['height']}+{self.cfg['x']}+{self.cfg['y']}")
        # resizable
        self.resizable(width=self.cfg['resizable_w'], height=self.cfg['resizable_h'])

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
        self.current_frame.frame_load()
        self.current_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def check_cfg(self):
        # 游戏路径检测
        pass

    def start_game(self):
        info_window = frames.ToplevelWindow(self)
        info_window.renew_info()
        thread = threading.Thread(target=self.character.script_start())
        thread.daemon = True  # 使线程在退出时自动清理
        thread.start()


def end_sign():
    pass


if __name__ == "__main__":
    # utils.require_admin()
    App = Tools()
    App.mainloop()
    # print('mainloop')
    # tools.box_draw(0, 0, 100, 100, 'red', 2)
    # print('box_draw')
    # time.sleep(2)
    # print('time sleep 2')
    # tools.box_hidden()
    # print('box_hidden')
    # time.sleep(2)
    # print('time sleep 2')
    # tools.box_draw(0, 0, 100, 100, 'red', 2)
    # print('box_draw')

