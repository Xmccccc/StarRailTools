# info 信息
# import time
# import json
# from pynput import mouse, keyboard
import json

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
           frames.FrameRunningInfo,  # 运行信息
           ]


class Character:
    def __init__(self):
        self.running = False  # 游戏是否运行
        self.minimize = False  # 游戏是否最小化
        self.position = 'none'  # 当前位置
        self.positions = '星轨航图'  # 星轨航图  导航-空间站黑塔  主控舱段  暂停  设置  声音  画面
        self.energy = 0  # 能量、体力
        self.stored_energy = 0  # 储存能量、储存体力
        self.money = 0  # 钱、金币


# 界面管理   包含图标、地图、导航等界面及图标
class InterfaceManage:
    def __init__(self, parent):
        self.parent = parent
        self.icon = {}  # 小图标 - 用于定位识别等 - 未添加
        self.text = {}  # 文本 - 用于定位识别等 - 未添加
        self.star_orbital_map = None  # 星轨航图  dict
        self.star_rail_map = None  # 星穹列车  dict
        self.maps = {}  # 大地图  dict

    def load_maps(self, ):
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


def end_sign():
    pass


if __name__ == '__main__':
    # interface_manage = InterfaceManage()
    # interface_manage.load_map_from_json()
    # maps_id_list = interface_manage.get_maps_id()
    # print(maps_id_list)
    pass

