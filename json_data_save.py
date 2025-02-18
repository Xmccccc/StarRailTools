import time

import cv2

import tools
import utils
# import matplotlib.pyplot as plt

config = {"path": r'cfg\config.json',
          # 数据加载
          "paths": {"ico": r'cfg\img\appicon.ico',
                    "zh": r'cfg\language\zh.json',
                    "en": r'cfg\language\en.json',
                    "intf": r'cfg\intf.json',
                    "intf_element": r'cfg\intf_element.json',
                    "img": r'cfg\img',
                    "intf_img_common_path": r'cfg\img\zh\intf',
                    "exe": r'C:\Program Files\miHoYo Launcher\games\Star Rail Game\StarRail.exe',

                    "maps_data": r'cfg\maps\data',
                    "star_orbital_map": r'cfg\maps\data\star_orbital_map.json',  # 星轨航图
                    "star_rail_map": r'cfg\maps\data\star_rail_map.json',  # 星穹列车
                    },

          "exe_name": 'StarRail.exe',
          "window_title": '崩坏：星穹铁道',

          # 窗口设置
          "title": 'StarRailTools V0.1',
          "language": 'zh',
          "width": 800,  # 窗口宽高
          "height": 600,
          "x": 100,  # 窗口距屏幕左上角距离
          "y": 100,
          "resizable_w": None,  # 窗口宽高是否固定
          "resizable_h": None,
          "font": "微软雅黑",  # 字体
          "font_size": 14,  # 字体大小

          # 运行设置
          "running_in_front": True,  # 是否前台运行
          "log_info_num": 6,  # 信息显示数量

          }

task = {'dig': 'all',
        "story": 'all',  # 剧情
        "simulated_universe": 'all',  # 模拟宇宙
        "forgotten_hall": 'all',  # 忘却之庭

        }

# 定位图片
position_img = {"launch": r'cfg\img\icon\game_launch.png',  # 开始游戏界面
                "stop": r'cfg\img\icon\.png',  # esc暂停、功能选择界面
                "star_orbital_map": r'cfg\img\icon\star_orbital_map.png',  # 星轨航图界面
                "star_rail_map": r'cfg\img\icon\star_orbital_map.png',  # 星穹列车界面

                }

# 图标图片
ico_img = {}

# 日常图片？ - 放在图标？
daily_img = {}

zh = {"function": '功能',
      "dig": '锄地',
      "story": '剧情',
      "simulated_universe": '模拟宇宙',
      "forgotten_hall": '忘却之庭',
      "run_all": '全部执行',
      "run_selected": '选择执行',

      "theme": '主题',

      "settings": '设置',

      "about": '关于',

      "map_choice": '地图选择',
      "status": '状态',
      "selected_all": '选择全部',

      "running_info": "运行信息",

      "program": '程序',
      "game": '游戏',
      "screenshot": '截图',
      "window": '窗口',
      "window_info": '窗口信息',
      "loc": '位置',
      "interface": '界面',

      "start": '启动',
      "no_start": '未启动',
      "starting": '启动中',
      "started": '已启动',
      "success": '成功',
      "fail": '失败',
      "minimizing": '最小化中',
      "minimized": '已最小化',
      "get": '获取',
      "getting": '获取中',
      "got": '获取成功',
      "match": '匹配',
      "matching": '匹配中',
      "matched": '匹配完成',
      "mark": '标记',
      "marking": '标记中',
      "marked": '标记完成',
      "recognize": '识别',
      "recognizing": '识别中',
      "recognized": '识别完成',
      "front": '最前',

      }

en = {"function": 'function',
      "dig": 'Dig',
      "story": 'Story',
      "simulated_universe": 'Simulated Universe',
      "forgotten_hall": 'Forgotten Hall',
      "run_all": 'Run All',
      "run_selected": 'Run Selected',

      "theme": 'Theme',

      "settings": 'Settings',

      "about": 'About',

      "map_choice": 'Map Choice',

      "running_info": "Running Info",

      "running": 'running',
      "no_running": 'no_running',
      "launch_T": 'Launch Failed',
      "launch_F": 'Launch Successfully',

      }

intf = [{'available': True,
         'independent': True,
         'next_intf': [],
         'id': '0000',
         'name': 'launch',  # 启动界面
         'sign_img_id': ['0000', ],

         },

        {'available': True,
         'independent': True,
         'next_intf': [],
         'id': '0001',
         'name': 'phone',  # 手机呼出界面
         'sign_img_id': ['0001', ],

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0002',
         'name': 'store01',  # 商店-推荐界面
         'sign_img_id': ['0002', ],

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0003',
         'name': 'store02',  # 商店-星芒兑换界面
         'sign_img_id': ['0003', ],

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0004',
         'name': 'store03',  # 商店-余烬兑换界面
         'sign_img_id': ['0004', ],

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0005',
         'name': 'store04',  # 商店-协议商店界面
         'sign_img_id': r'cfg\img\zh\intf\intf0005.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0006',
         'name': 'store05',  # 商店-捕获梦华界面
         'sign_img_id': r'cfg\img\zh\intf\intf0006.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0007',
         'name': 'store06',  # 商店-星琼购买界面
         'sign_img_id': r'cfg\img\zh\intf\intf0007.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0008',
         'name': 'friends01',  # 好友-我的好友界面
         'sign_img_id': r'cfg\img\zh\intf\intf0008.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0009',
         'name': 'friends02',  # 好友-萍水相逢界面
         'sign_img_id': r'cfg\img\zh\intf\intf0009.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0010',
         'name': 'entrust01',  # 委托-专属材料界面
         'sign_img_id': r'cfg\img\zh\intf\intf0010.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0011',
         'name': 'entrust02',  # 委托-经验材料/信用点界面
         'sign_img_id': r'cfg\img\zh\intf\intf0011.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0012',
         'name': 'entrust02',  # 委托-合成材料界面
         'sign_img_id': r'cfg\img\zh\intf\intf0012.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0012',
         'name': 'entrust02',  # 委托-合成材料界面
         'sign_img_id': r'cfg\img\zh\intf\intf0012.png',

         },

        {'available': True,
         'independent': True,
         'next_intf': [],
         'id': '0013',
         'name': 'entrust03',  # 委托-委托报告界面 - 领取委托奖励界面
         'sign_img_id': r'cfg\img\zh\intf\intf0013.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0014',
         'name': 'navigation01',  # 导航-星轨航图界面
         'sign_img_id': r'cfg\img\zh\intf\intf0014.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0015',
         'name': 'navigation02',  # 导航-空间站黑塔-主控舱段界面
         'sign_img_id': r'cfg\img\zh\intf\intf0015.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0016',
         'name': 'navigation03',  # 导航-空间站黑塔-基座舱段界面
         'sign_img_id': r'cfg\img\zh\intf\intf0016.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0016',
         'name': 'navigation04',  # 导航-空间站黑塔-收容舱段2层界面
         'sign_img_id': r'cfg\img\zh\intf\intf0017.png',

         },

        {'available': True,
         'independent': False,
         'next_intf': [],
         'id': '0017',
         'name': 'navigation05',  # 导航-空间站黑塔-收容舱段1层界面
         'sign_img_id': r'cfg\img\zh\intf\intf0017.png',

         },

        ]


intf_element = {'0001': [{'element_id': '01_00',
                          'element_name': 'esc',
                          'element_type': 'key',
                          'target_intf': 'last_independent_intf',  # last_independent_intf  last_intf  返回上一独立界面还是上一界面
                          'img_id': None,
                          'offset': None,
                          },

                         {'element_id': '01_01',
                          'element_name': 'friends',
                          'element_type': 'button',
                          'target_intf': 'friends',
                          'img_id': [r'cfg\img\zh\intf\intf01_01.png', ],
                          'offset': (0, 0),
                          },

                         {'element_id': '01_02',
                          'element_name': 'friends',
                          'element_type': 'button',
                          'target_intf': 'friends',
                          'img_id': [r'cfg\img\zh\intf\intf01_01.png', ],
                          'offset': (0, 0),
                          },

                         ],
                }



def end_sign():
    pass


if __name__ == '__main__':
    files_info = [(config, r'cfg\config.json'),
                  (task, r'user_cfg\task\task.json'),
                  (zh, r'cfg\language\zh.json'),
                  (en, r'cfg\language\en.json'),
                  (intf, r'cfg\intf.json'),

                  ]

    for file, path in files_info:
        utils.save_json_file(path, file)

    # for key in star_orbital_map:
    #     print(key)
    #     print(type(key))

    # 尝试运行
    # if not utils.is_running(config['exe_name']):
    #     utils.program_launch(config['paths']['exe'])
    #     time.sleep(5)
    # window = utils.get_window(config['window_title'])
    # if not window:
    #     print('窗口获取失败')
    #     window_rect = None
    #     input()
    # else:
    #     print(f'window:\n{window}')
    #     window.activate()
    #     window_rect = utils.get_window_rect(window)
    #
    # if not window_rect:
    #     print('窗口信息获取失败')
    #     img = None
    #     input()
    # else:
    #     print(f'window_rect:\n{window_rect}')
    #     img = utils.capture_window(window_rect)
    #
    # while True:
    #     image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     plt.imshow(image_rgb)
    #     plt.axis('off')  # 隐藏坐标轴
    #     plt.show()
    #     key = cv2.waitKey(0)  # 按下任意按键后继续执行
    #     if key == 27:  # 如果按下 'esc' 键
    #         break
    #     plt.close()
    #     # plt.close('all')
    #     time.sleep(1)
    #     img = utils.capture_window(window_rect)

    pass
