import utils

config = {"title": 'StarRailTools V0.1',
          "language": 'zh',
          "width": 800,  # 窗口宽高
          "height": 600,
          "x": 100,  # 窗口距屏幕左上角距离
          "y": 100,
          "font": "微软雅黑",
          "font_size": 14,

          }

zh = {"function": '功能',
      "theme": '主题',
      "settings": '设置',
      "about": '关于',
      "dig": '锄地',
      "story": '剧情',
      "simulated_universe": '模拟宇宙',
      "forgotten_hall": '忘却之庭',
      "run_all": '全部执行',
      "run_selected": '选择执行',
      "map_choice": '地图选择',
      }

en = {"function": 'function',
      "theme": 'Theme',
      "settings": 'Settings',
      "about": 'About',
      "dig": 'Dig',
      "story": 'Story',
      "simulated_universe": 'Simulated Universe',
      "forgotten_hall": 'Forgotten Hall',
      "run_all": 'Run All',
      "run_selected": 'Run Selected',
      "map_choice": 'Map Choice',
      }

file = config
strings = 'config'

path = f'cfg/{strings}.json'
utils.save_json_file(path, file)
