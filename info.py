# info 信息
# import time
# import json
# from pynput import mouse, keyboard
import frames

left_menu_list = [frames.FrameTools,
                  frames.FrameTheme,
                  frames.FrameSetting,
                  frames.FrameAbout,
                  ]

fc_list = [frames.FrameTools,
           frames.FrameTheme,
           frames.FrameSetting,
           frames.FrameAbout,
           frames.FrameDig,
           frames.FrameStory,
           frames.FrameSimulatedUniverse,
           frames.FrameForgottenHall,
           ]


class MapInfo:
    def __init__(self):
        self.map01 = {"name": '空间站',

                      }


class CharacterInfo:
    def __init__(self):
        self.position = 'none'  # 当前位置
        self.energy = 0  # 能量、体力
        self.stored_energy = 0  # 储存能量、储存体力
        self.money = 0  # 钱、金币
