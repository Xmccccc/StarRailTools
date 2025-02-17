# utils 基础组件 - 可通用
import os
import sys
import time
import json
import ctypes
import tkinter as tk
from tkinter import ttk

import psutil
import win32gui
import win32con
import cv2 as cv
import pygetwindow as gw
from pywinauto import Application
import mss


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


def text_save(path, text, time_stamp=True):
    if time_stamp:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        text = f"[{current_time}]\t{text}"
    with open(path, 'a') as file:
        file.write(text + '\n')


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


def is_program_running(exe_name):
    """
    判断程序是否运行
    :param exe_name:
    :return:
    """
    for proc in psutil.process_iter(['name']):
        if exe_name.lower() in proc.info['name'].lower():  # StarRail.exe  忽略大小写
            return True
    return False


def minimize_window(window_title):
    """
    最小化程序窗口
    :param window_title:
    :return:
    """
    try:
        window = gw.getWindowsWithTitle(window_title)[0]  # 获取窗口句柄
        window.minimize()
        return True
    except IndexError:  # 未找到窗口
        return False


def launch_program(exe_path):
    """
    启动路径程序
    :param exe_path:
    :return:
    """
    os.startfile(exe_path)


def end_sign():
    pass


if __name__ == '__main__':
    # launch_program()
    pass
