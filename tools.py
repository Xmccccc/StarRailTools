# tools 项目工具
# import time
# import json
# from pynput import mouse, keyboard
import json
import time
import threading
from dataclasses import dataclass
from typing import Dict, Optional, List

import frames
import utils

left_menu_list = [frames.FrameTools,
                  frames.FrameTheme,
                  frames.FrameSetting,
                  frames.FrameAbout,
                  ]

fc_list = [frames.FrameTools,  # 功能
           frames.FrameTheme,  # 主题
           frames.FrameSetting,  # 设置
           frames.FrameAbout,  # 关于
           frames.FrameDig,  # 锄地
           frames.FrameStory,  # 剧情
           frames.FrameSimulatedUniverse,  # 模拟宇宙
           frames.FrameForgottenHall,  # 忘却之庭
           ]


@dataclass
class Element:
    """界面元素数据基类"""
    element_id: str  # 检索图片名用?
    element_name: str  # 名字 - 点击***按钮、按下***键  例: '好友'、'esc'
    element_type: str = 'button'  # button、key  界面按钮或者键盘指令
    target_intf: str = None  # 点击界面按钮或输入键盘指令后跳转的目标界面名称name   last_independent_intf、last_intf - 返回上一独立界面还是上一界面
    img_id: Optional[List[str]] = None  # 界面按钮图片路径列表 - 可能需要点击多次才能进入下一界面
    offset: Optional[tuple] = (0, 0)  # 点击位置偏移 - 默认中心
    # threshold: Optional[float] = 0.8  # 匹配阈值


class IntfBase:
    """界面基类"""
    def __init__(self, info):
        self.available = info['available'] if 'available' in info else True  # 是否废弃 - 活动界面等 - 过期即消失
        self.independent = info['independent'] if 'independent' in info else False  # 是否独立界面 - 判断esc返回的上一个界面是什么
        self.next_intf = info['next_intf'] if 'next_intf' in info else None  # 存储此界面能进入的下一个界面id - 减少截图对比数量
        self.id = info['id'] if 'id' in info else None
        self.name = info['name'] if 'name' in info else None
        self.sign_img_id= info['sign_img_id'] if 'sign_img_id' in info else None
        self.is_gray = info['is_gray'] if 'is_gray' in info else False  # 是否使用灰度图片匹配截图
        self.element: List[Element]


# 界面管理   包含图标、地图、导航等界面及图标
class IntfManage:
    def __init__(self, parent):
        self.parent = parent
        self.intf_info = self.parent.intf_info
        self.intf_element_info = self.parent.intf_element_info
        self.intf = []  # 所有界面
        self.last_independent_intf = None  # 上一个独立界面
        self.last_intf = None  # 上一个界面
        self.current_intf = None  # 当前界面
        self.next_intf = None  # 下一个将要进入界面
        self.intf_img_common_path = r'cfg\pictures\zh\intf',

        self.icon = {}  # 小图标 - 用于定位识别等 - 未添加
        self.text = {}  # 文本 - 用于定位识别等 - 未添加
        self.star_orbital_map = None  # 星轨航图  dict
        self.star_rail_map = None  # 星穹列车  dict
        self.maps = {}  # 大地图  dict

    def load_intf(self, ):
        """
        加载界面信息
        :return:
        """
        for intf in self.intf_info:
            intf_instance = IntfBase(intf)
            intf_id = intf_instance.id
            if intf_id in self.intf_element_info:
                intf_instance.element = []
                for element in self.intf_element_info[intf_id]:
                    intf_instance.element.append(Element(
                        element_id=element['element_id'],
                    ))1111
            else:
                intf_instance.element = None
            self.intf.append(intf_instance)

        self.star_orbital_map = utils.load_json_file(self.parent.cfg['paths']['star_orbital_map'])
        self.star_rail_map = utils.load_json_file(self.parent.cfg['paths']['star_rail_map'])

        path_ = self.parent.cfg['paths']['maps_data']
        for key in self.star_orbital_map:
            path = f"{path_}\\map{key}.json"
            name = self.star_orbital_map[key]['name_zh']
            dic = utils.load_json_file(path)
            self.maps[name] = dic  # key: name_zh   value: dict map01、map02...

    def search_maps(self, target='id'):

        maps_id = []
        for key in self.maps:
            maps_id.append(key)
        return maps_id


class Character:
    def __init__(self, parent):
        self.parent = parent
        self.text = self.parent.text
        # 窗口信息
        self.app = None  # pywinauto的app对象
        self.window = None  # app对象的window实例
        self.window_hwnd = None  # 窗口句柄
        self.window_rect = None  # 窗口的位置尺寸 - Left-top-width-height
        # 运行参数
        self.running = False  # 游戏是否运行
        self.minimize = False  # 游戏是否最小化

        self.status = None  # 角色当前状态(更新日志) - 游戏启动中、切换地图中、锄地中
        self.new_status = None
        self.position = None  # 位置 - 星轨航图、大地图: 空间站黑塔-主控舱段   由pictures-icon定位
        # self.positions = '星轨航图'  # 星轨航图  导航-空间站黑塔  主控舱段  暂停  设置  声音  画面
        self.energy = 0  # 能量、体力
        self.stored_energy = 0  # 储存能量、储存体力
        self.money = 0  # 钱、金币

        self.st = 0.1  # stop time  暂停时间
        self.screenshot = None  # 截图
        self.threshold = 0.8  # 置信度
        self.screen_loc = None  # 基于截图的模板图片匹配区域坐标
        self.box_loc = None  # 区域距屏幕左上角距离: (x, y, width, height)
        self.val = None  # 截图匹配置信度、匹配度
        self.mouse_loc = None  # 基于窗口的鼠标位置

    def script_start(self):
        task_list = self.parent.task_list
        task_info = self.parent.task_info
        self.game_launch()
        if 'dig' in task_list:
            self.dig()

    def get_position(self):
        pass

    def game_launch(self):
        self.is_running()
        while not self.running:
            self.program_launch()
            self.is_running()
        self.get_window_info()
        self.window_front()

    def dig(self):
        pass

    def is_running(self):
        self.running = utils.is_running(self.parent.cfg['exe_name'])
        if self.running:
            self.new_status = self.text['game'] + self.text['started']
        else:
            self.new_status = self.text['game'] + self.text['no_start']
        self.renew_log(st=self.st)

    def program_launch(self):
        utils.program_launch(self.parent.cfg['paths']['exe'])
        self.new_status = self.text['game'] + self.text['starting']
        self.renew_log(st=10)

    def get_window_info(self):
        self.new_status = self.text['game'] + self.text['started']
        self.renew_log()
        hwnd, rect = utils.get_window_info(self.parent.cfg['window_title'])
        if hwnd:
            self.window_hwnd = hwnd
            self.window_rect = rect
            self.app, self.window = utils.get_app_window(hwnd)

    def window_front(self):
        utils.window_front(self.window_hwnd)
        self.new_status = self.text['window'] + self.text['front']
        self.renew_log(st=self.st)

    def capture_window(self, full_screen=False):
        self.screenshot = utils.capture_window(self.window_rect, full_screen)  # 获取截图

    def img_comparison(self, picture_path, gray=True):
        self.new_status = self.text['interface'] + self.text['recognizing']
        self.renew_log(st=self.st)
        loc, val = utils.img_match(self.screenshot, picture_path, gray)
        if val >= self.threshold:  # 大于等于置信度/匹配度
            self.screen_loc = loc
            self.val = val
            x = self.screen_loc[0] + self.window_rect[0]
            y = self.screen_loc[1] + self.window_rect[1]
            width = self.screen_loc[3]
            height = self.screen_loc[4]
            self.box_loc = (x, y, width, height)
        #     self.new_status = self.text['match'] + self.text['success'] + f": {val}"
        # else:
        #     self.new_status = self.text['match'] + self.text['fail'] + f": {val}"
        # self.renew_log(st=self.st)

    def hollow_box_move(self):
        self.parent.info_show.canvas_setting(self, self.box_loc)

    def hollow_box_clear(self):
        self.parent.info_show.canvas.delete('all')

    def get_mouse_loc(self):
        self.mouse_loc = utils.get_center_loc(self.screen_loc)  # 元组

    def mouse_move(self):
        self.window.move_mouse(coords=self.mouse_loc)
        time.sleep(0.1)

    def mouse_click(self, click='left'):
        if click == 'left':  # 左键点击
            self.window.click_input()
        elif click == 'right':  # 右键点击
            self.window.right_click_input()
        time.sleep(0.1)

    def mouse_scroll(self, scroll):
        self.window.scroll(scroll)
        time.sleep(0.1)

    def lock_and_click(self, ):
        pass

    def renew_log(self, st=0.0, time_stamp=True):
        """
        log信息更新
        :param st: 暂停时间
        :param time_stamp: 是否记录时间戳
        :return:
        """
        if self.status != self.new_status:
            self.status = self.new_status
            text = f"当前状态:  " + self.status
            self.parent.log_info = utils.save_show_text(self.parent.log_path, self.parent.log_info, text, time_stamp)
            time.sleep(st)


def end_sign():
    pass


if __name__ == '__main__':
    # interface_manage = InterfaceManage()
    # interface_manage.load_map_from_json()
    # maps_id_list = interface_manage.get_maps_id()
    # print(maps_id_list)
    pass

