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

    def frame_load(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_frame_callback(self, fc):  # fc: frame class
        self.parent.show_frame(fc)


class FrameTools(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["function"]  # 进入此界面的按钮文本
        self.buttons = []

    def frame_load(self):
        super().frame_load()  # 调用父类方法

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
                text=frame_cls(self.parent).name,
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

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # button
        button01 = tk.Button(self, text="主题")
        button01.pack()


class FrameSetting(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["settings"]  # 进入此界面的按钮文本

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # button
        button01 = tk.Button(self, text="设置")
        button01.pack()


class FrameAbout(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["about"]  # 进入此界面的按钮文本

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # button
        button01 = tk.Button(self, text="关于")
        button01.pack()


class FrameDig(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["dig"]  # 锄地
        self.hovered_item = None  # 记录鼠标悬停位置
        self.selected = '☑'
        self.unselected = '☐'

        self.style = ttk.Style()
        # widget
        # self.labels = [None]  # labels
        self.tree = None  # treeview
        self.buttons = []  # buttons

        self.dig_maps = {}  # key: name  value: name   all maps
        self._get_dig_maps()  # 锄地地图结构获取
        self.select_maps = {}

    def frame_load(self):
        super().frame_load()  # 调用父类方法
        self._style_set()
        self._labels_set()
        self._tree_set()
        self._buttons_set()

    def _style_set(self):
        self.style.configure("Treeview",
                             font=(self.parent.cfg['font'], 12),
                             rowhight=30)  # problem - 每一行不够宽

        self.style.configure("Treeview.Heading",
                             font=(self.parent.cfg['font'], 14, "bold"),  # 表头文字加粗14号
                             foreground="black")  # 表头文字颜色

    def _labels_set(self):
        self.label = tk.Label(self, text=self.name,
                              bd=1, relief="ridge",
                              font=(self.font, 20, 'bold'),)
        # self.label.grid(row=0, column=0, padx=10, pady=5, fill='both')  # sticky="w"将文本靠左对齐
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')  # sticky="w"将文本靠左对齐
        self.grid_rowconfigure(0, minsize=50, weight=0)
        self.grid_columnconfigure(0, minsize=100, weight=1)

    def _tree_set(self):
        self.tree = ttk.Treeview(
            self,
            columns=("status",),  # 除#0外，只显示一列，即values的第一个元素
            show="tree headings",
            selectmode="none"
        )
        # 配置列参数
        self.tree.heading("#0", text=self.text['map_choice'])  # 地图选择
        self.tree.heading("status", text=self.text['status'])  # 状态
        self.tree.column("#0", width=260, stretch=True)
        self.tree.column("status", width=30, anchor="center")

        # 设置默认背景颜色
        self.default_bg = self.tree.tag_configure("default", background="white", foreground='black')  # 默认
        self.hover_bg = self.tree.tag_configure("hover", background="#e0e0e0", foreground='black')  # 鼠标悬停
        self.selected_bg = self.tree.tag_configure('selected', background='#A0A0A0', foreground='black')  # 选中

        self._tree_data_set()  # 数据配置
        self.tree.bind("<Motion>", self._on_mouse_move)  # 鼠标进入treeview事件
        self.tree.bind("<Leave>", self._on_mouse_leave)  # 鼠标离开treeview事件
        self.tree.bind("<Button-1>", self._on_click)  # 左键点击事件
        # self.tree.grid(row=1, column=0, columnspan=2, sticky="nsew", fill='both')  # grid布局
        self.tree.grid(row=1, column=0, columnspan=2, sticky="nsew")  # grid布局
        self.grid_rowconfigure(1, minsize=50, weight=1)
        self.grid_columnconfigure(1, minsize=100, weight=1)

    def _tree_data_set(self):
        for main_map_name in self.dig_maps:
            c1 = self.tree.insert('', 'end', text=main_map_name, values=[self.unselected, ], tags='default')

            self.tree.tag_configure(main_map_name, background='white', foreground='black')  # black
            for sub_map in self.dig_maps[main_map_name]:
                self.tree.insert(c1, 'end', text=sub_map, values=[self.unselected, ], tags='default')
                self.tree.tag_configure(sub_map, background='white', foreground='black')  # white

    def _on_mouse_move(self, event):
        item = self.tree.identify_row(event.y)

        if not item:  # 如果没有新行被识别，直接返回
            return

        if item != self.hovered_item:  # 如果当前行与上次悬停的行不同，则更新背景颜色
            if self.hovered_item:  # 恢复上一个悬停行的背景颜色
                if 'selected' not in self.tree.item(self.hovered_item, 'tags'):
                    self.tree.item(self.hovered_item, tags="default")

            # 更新当前悬停行的背景颜色
            if 'selected' not in self.tree.item(item, 'tags'):
                self.tree.item(item, tags="hover")

            self.hovered_item = item  # 更新悬停的项目

    def _on_mouse_leave(self, event):
        # 鼠标离开时，恢复背景颜色
        if self.hovered_item:
            if 'selected' not in self.tree.item(self.hovered_item, 'tags'):
                self.tree.item(self.hovered_item, tags="default")
        self.hovered_item = None
        pass

    def _on_click(self, event):
        region = self.tree.identify("region", event.x, event.y)  # region区域: heading  tree  cell  str
        column = self.tree.identify_column(event.x)  # column列: #0  #1  str  --  无作用？
        item = self.tree.identify_row(event.y)  # 节点item (heading为空) sb. I001  I00C  str  每行相同

        if region == 'tree':  # 第一列
            if self.tree.get_children(item):  # 含子节点/子地图
                self._expansion(item)  # 展开 - 折叠
            else:  # 子地图 - 状态改变 - 勾选改变
                value = self._value_change(item)
                self._status_change(item, value)
                self._selected_check(item, value)
        elif region == 'cell':  # 第二列 - 状态改变 - 勾选改变
            value = self._value_change(item)
            self._status_change(item, value)
            self._selected_check(item, value)

    def _expansion(self, item):
        if self.tree.item(item, 'open'):
            self.tree.item(item, open=False)  # 折叠
        else:
            self.tree.item(item, open=True)  # 展开

    def _value_change(self, item):
        value = self.tree.item(item, 'values')[0]
        value = self.unselected if value == self.selected else self.selected
        return value

    def _status_change(self, item, value):
        self.tree.item(item, values=(value, ))
        self._color_change(item, value)

    def _selected_check(self, item, value):
        if self.tree.get_children(item):  # 含有子节点 - 更改其子节点value
            for child in self.tree.get_children(item):
                self._status_change(child, value)
                child_value = self.tree.item(child, 'values')[0]
                self._selected_check(child, child_value)
        else:  # 检测是否有父节点 - 父节点value更改
            parent = self.tree.parent(item)
            children = self.tree.get_children(parent)
            values_list = []
            for child in children:
                values = self.tree.item(child, 'values')
                values_list.append(values[0])  # 列表添加values元组第一个元素
            if self.unselected in values_list:
                self._status_change(parent, self.unselected)
            if all(x == values_list[0] for x in values_list):
                self._status_change(parent, values_list[0])

    def _color_change(self, item, value):
        if value == self.selected:
            self.tree.item(item, tags='selected')
        elif value == self.unselected:
            self.tree.item(item, tags='default')

    def _buttons_set(self):
        # button info
        buttons_info = [
            (self._selected_all, self.text['selected_all'], 3, 0),
            (self.dig, self.text['start'], 3, 1),
        ]

        # button
        for func, text, row, col in buttons_info:
            btn = tk.Button(
                self,
                text=text,
                command=func,
                # bg='#2d2d2d',
                # fg='white',
                # activebackground='#404040',
                padx=10,
                pady=6,
                width=6,
                height=1,
                font=(self.font, self.font_size))  # 微软雅黑  Georgia  14
            btn.grid(row=row, column=col, sticky="nsew")
            self.grid_rowconfigure(row, minsize=50, weight=0)
            self.grid_columnconfigure(col, minsize=100, weight=1)
            self.buttons.append(btn)

    def _selected_all(self):

        pass

    def dig(self):
        self._get_selected_maps()

    def _get_selected_maps(self):
        pass

    def _get_dig_maps(self):
        star_orbital_map = self.parent.intf_mgr.star_orbital_map
        maps = self.parent.intf_mgr.maps  # key: name_zh  value: dict

        for key in star_orbital_map:
            main_map_name = star_orbital_map[key]['name_zh']
            self.dig_maps[main_map_name] = []
            for sub_map_id in star_orbital_map[key]['sub_maps_id']:
                if maps[main_map_name][sub_map_id]['monster']:
                    sub_map_name_ = maps[main_map_name][sub_map_id]['name_zh']
                    if maps[main_map_name][sub_map_id]['layer']:
                        for floor in maps[main_map_name][sub_map_id]['layer']:
                            sub_map_name = f"{sub_map_name_}{floor}层"
                            self.dig_maps[main_map_name].append(sub_map_name)
                    else:
                        self.dig_maps[main_map_name].append(sub_map_name_)


class FrameStory(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["story"]  # 剧情

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # button info

        tk.Button(self, text=self.name, command=lambda: print(self.name),
                  width=8, height=1, font=('Georgia', 14)).grid()


class FrameSimulatedUniverse(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["simulated_universe"]  # 模拟宇宙

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # button info

        # button
        button01 = tk.Button(self, text="模拟宇宙")
        button01.pack()


class FrameForgottenHall(FrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.name = self.text["forgotten_hall"]  # 忘却之庭

    def frame_load(self):
        super().frame_load()  # 调用父类方法

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
        self.labels = []  # 运行信息显示label
        self.run_info = []  # 运行信息列表 - 弃掉旧信息
        self.info_num = self.parent.cfg["info_num"]  # 信息显示条数

    def frame_load(self):
        super().frame_load()  # 调用父类方法

        # show info labels
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
