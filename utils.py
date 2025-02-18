# utils 基础组件 - 可通用
import os
import sys
import time
import json
import ctypes
import threading
import tkinter as tk
from tkinter import ttk

import psutil
import win32gui
import win32con
import numpy as np

import mss
import cv2
# import pyautogui
import pygetwindow as gw
import pywinauto
from pywinauto import application
from pywinauto import mouse


class InfoShow:  # InfoShow
    def __init__(self, parent):
        """
        信息显示
            - 左下角显示当前状态： 当前任务、位置、状态、、、
            - 空心框标记识别位置
        """
        self.parent = parent

        # 创建顶层窗口 - 独立子窗口 - 空心框创建
        self.canvas_window = tk.Toplevel()
        self._init_canvas_window()  # # 初始化空心框窗口

        # 创建顶层窗口 - 独立子窗口 - 信息显示窗口
        self.info_window = tk.Toplevel()
        self._init_info_window()  # # 初始化信息窗口

    def _init_canvas_window(self):
        self.canvas_window.geometry(f"{0}x{0}+{0}+{0}")  # 设置窗口尺寸位置
        self.canvas_window.overrideredirect(True)  # 去除标题栏及边框 - 无边框窗口
        self.canvas_window.attributes('-topmost', True)  # 窗口置顶显示 - 显示在其他窗口前面
        self.canvas_window.attributes('-transparentcolor', 'white')  # 设置窗口白色部分透明 - 空心效果

        self.canvas = tk.Canvas(self.canvas_window, bg='white', highlightthickness=0)  # white

        # 设置鼠标穿透 - 空心框穿透
        if sys.platform == 'win32':  # 判断是否为windows系统
            self._set_click_through_win()

    def _init_info_window(self):
        """初始化信息显示窗口"""
        info_width = 200  # 信息窗口宽度
        info_height = 300  # 信息窗口高度
        label_bg = '#404040'  # 深灰色背景-2C2C2C  404040

        # 获取屏幕尺寸
        screen_width = self.info_window.winfo_screenwidth()
        screen_height = self.info_window.winfo_screenheight()

        # 定位到左下角
        self.info_window.geometry(f"{info_width}x{info_height}+20+{screen_height - info_height - 50}")  # 设置窗口尺寸位置
        self.info_window.overrideredirect(True)  # 去除标题栏及边框 - 无边框窗口
        self.info_window.attributes('-topmost', True)  # 窗口置顶显示 - 显示在其他窗口前面
        self.info_window.attributes('-transparentcolor', 'white')  # 设置窗口白色部分透明 - 空心效果
        self.info_window.configure(bg='white')  # 深灰色背景 - 2C2C2C

        # 信息标签容器
        self.info_frame = tk.Frame(
            self.info_window,
            bg='white',
            padx=10,
            pady=10
        )
        self.info_frame.pack(expand=True, fill='both')

        # 初始化信息标签
        self.labels = {
            'task': tk.Label(
                self.info_frame,
                text="[当前任务]: None",  # 锄地、、、
                fg='#A0DCF2',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'position': tk.Label(
                self.info_frame,
                text="[位置]: None",  # 空间站黑塔-主控舱段、、、
                fg='#00FF00',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'status': tk.Label(
                self.info_frame,
                text="[状态]: None",  # 切换地图中、战斗中、、、
                fg='#FF3333',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'log_info': tk.Label(
                self.info_frame,
                text="运行信息:",
                fg='#CC6600',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
        }

        for ind in range(self.parent.log_info_num):
            label = tk.Label(
                self.info_frame,
                text=f"    默认消息{ind+1}",  # 切换地图中、战斗中、、、
                fg='#FFA500',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            )
            label_name = f'log{ind+1}'
            self.labels[label_name] = label
        # 布局标签
        for label in self.labels.values():
            label.pack(fill='x', pady=1)

    def update_info(self, task=None, position=None, status=None, log=None):
        self.labels['task'].config(text=f"[当前任务]: {task}")
        self.labels['position'].config(text=f"[位置]: {position}")
        self.labels['status'].config(text=f"[状态]: {status}")
        # log info ---  error
        self.labels['log1'].config(text=f"    {log}")

    def canvas_setting(self, box_loc, border_color='red', border_width=1):
        """
        空心框设置
        :param box_loc:空心框左上角x、y坐标; 空心框宽度width、高度height
        :param border_color: 空心框颜色（默认红色）
        :param border_width: 空心框线框宽度（默认1像素）
        :return:
        """
        x, y, width, height = box_loc
        self.canvas_window.geometry(f"{width}x{height}+{x}+{y}")
        self.canvas.delete('all')  # 清除原有图形
        self.canvas.create_rectangle(
            0, 0,
            width - border_width,
            height - border_width,
            outline=border_color,
            width=border_width
        )
        self.canvas.pack(fill='both', expand=True)

    def _set_click_through_win(self):
        """
        Windows系统设置鼠标穿透
        :return:
        """
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetParent(self.canvas_window.winfo_id())
            ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
            ex_style |= 0x00000020  # WS_EX_TRANSPARENT
            ex_style |= 0x00080000  # WS_EX_LAYERED
            ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style)
        except Exception as e:
            print(f"鼠标穿透设置失败: {e}")


def save_json_file(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=5)


def load_json_file(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"文件未找到:\n\t{path}\n")
    except json.JSONDecodeError:
        print(f"读取JSON文件时发生错误，文件内容可能无效:\n\t{path}\n")


def text_save_to_file(path, text, time_stamp=True):
    if time_stamp:  # 显示时间戳
        current_time = time.strftime("%H:%M:%S", time.localtime())
        text = f"[{current_time}]\t{text}"
    with open(path, 'a') as file:
        file.write(text + '\n')
    return text


def list_change(lst, info):
    """
    列表增加一个元素到末尾，删去第一个元素
    :param lst:
    :param info:
    :return:
    """
    lst.append(info)
    lst.pop(0)
    return lst


def save_show_text(path, lst, text, time_stamp=True):
    text_save_to_file(path, text, time_stamp)
    new_lst = list_change(lst, text)
    return new_lst


def require_admin():
    """
    获取管理员权限
    :return:
    """
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    if not admin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
        # print("以管理员权限运行成功！")
        # return
        sys.exit()


def is_running(exe_name):
    """
    判断程序是否运行
    :param exe_name:
    :return:
    """
    for proc in psutil.process_iter(['name']):
        if exe_name.lower() in proc.info['name'].lower():  # StarRail.exe  忽略大小写
            return True
    return False


def program_launch(exe_path):
    """
    启动路径程序
    :param exe_path:
    :return:
    """
    os.startfile(exe_path)


def get_window_info(window_title):
    hwnd = win32gui.FindWindow(None, window_title)  # 窗口不存在则返回0
    rect = None
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
    return hwnd, rect


def get_app_window(hwnd):
    app = application.Application().connect(handle=hwnd)
    window = app.window(handle=hwnd)
    return app, window


def window_front(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 恢复窗口
    # win32gui.SetForegroundWindow(hwnd)  # 将窗口置前


def capture_window(window_rect=None, full_screen=False):
    """
    截取窗口
    :param window_rect: 窗口尺寸位置信息
    :param full_screen: 是否截取全屏
    :return:
    """
    with mss.mss() as sct:
        if full_screen:
            monitor = sct.monitors[1]  # 选择主显示器
        else:
            if window_rect is None:  # 抛出异常
                raise ValueError("window_rect must be provided when full_screen is False.")
            left, top, width, height = window_rect
            monitor = {"top": top, "left": left, "width": width, "height": height}
        screenshot = sct.grab(monitor)  # 截取指定区域
        img = np.array(screenshot)  # 转为numpy数组
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 转换为BGR格式
    return img


def get_img(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    return img


def img_match(screenshot, template, gray=True):
    """
    将截图与现有图像对比
    :param screenshot: 截图
    :param template: 模板图片
    :param gray: 是否转化为灰度图
    :return:
    """

    if gray:
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    height, width = template.shape[:2]  # 匹配区域宽高

    location = (max_loc[0], max_loc[1], width, height)  # 匹配区域左上角在截图的坐标及宽高
    value = max_val
    return location, value  # 最佳匹配位置及匹配度


def get_center_loc(location):
    x, y, width, height = location
    x_center = x + width/2
    y_center = y + height/2
    return x_center, y_center


def end_sign():
    pass


if __name__ == '__main__':
    # app = tk.Tk()
    # app.log_info_num = 6
    # box = HollowBox(app)
    # app.box = box
    # # app.
    # app.mainloop()

    intf_info = load_json_file(r'cfg\intf.json')
    print(intf_info[0])
    print(type(intf_info[0]))
    print(intf_info[0]['id'])
    print(type(intf_info[0]['id']))
    print(intf_info[0]['available'])
    print(type(intf_info[0]['available']))
    pass
