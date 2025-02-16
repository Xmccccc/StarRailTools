import utils

config = {"path": r'cfg\config.json',
          # 数据加载
          "paths": {"ico": r'cfg\appicon.ico',
                    "zh": r'cfg\language\zh.json',
                    "en": r'cfg\language\en.json',
                    "maps_data": r'cfg\maps\data',
                    "star_orbital_map": r'cfg\maps\data\star_orbital_map.json',  # 星轨航图
                    "star_rail_map": r'cfg\maps\data\star_rail_map.json',  # 星穹列车
                    "map_pictures": r'cfg\maps\pictures',
                    "exe": r'C:\Program Files\miHoYo Launcher\games\Star Rail Game\StarRail.exe',
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
          "info_num": 6,  # 信息显示数量

          }

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
      "start": '启动',

      "running_info": "运行信息",

      "running": '程序运行中...',
      "no_running": '程序未启动...',
      "launch_S": '程序启动成功...',
      "launch_F": '程序启动失败...',
      "minimize_Run": '程序最小化中...',
      "minimize_S": '程序最小化成功...',

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

# 其他界面


# 导航界面  星轨航图
star_orbital_map = {"01": {"name_zh": '空间站黑塔',
                           "parent_map_name_zh": '星轨航图',
                           "id": '01',
                           "level": 1,
                           "pictures": None,  # 图片名字字典
                           "monster": True,  # 怪物
                           "book": True,  # 阅读物收集
                           "puzzle": True,  # 解密
                           "treasure": True,  # 宝箱
                           "sub_maps_id": ['0101', '0102', '0103', '0104', '0105'],
                           "layer": None,
                           },

                    "02": {"name_zh": '雅利洛',
                           "parent_map_name_zh": '星轨航图',
                           "id": '02',
                           "level": 1,
                           "pictures": None,
                           "monster": True,  # 怪物
                           "book": True,  # 阅读物收集
                           "puzzle": True,  # 解密
                           "treasure": True,  # 宝箱
                           "sub_maps_id": ['0201', '0202', '0203', '0204', '0205', '0206',
                                           '0207', '0208', '0209', '0210', '0211', '0212'],
                           "layer": None,
                           },

                    "03": {"name_zh": '仙舟罗浮',
                           "parent_map_name_zh": '星轨航图',
                           "id": '03',
                           "level": 1,
                           "pictures": None,
                           "monster": True,  # 怪物
                           "book": True,  # 阅读物收集
                           "puzzle": True,  # 解密
                           "treasure": True,  # 宝箱
                           "sub_maps_id": ['0301', '0302', '0303', '0304', '0305', '0306',
                                           '0307', '0308', '0309', '0310', '0311', '0312'],
                           "layer": None,
                           },

                    "04": {"name_zh": '匹诺康尼',
                           "parent_map_name_zh": '星轨航图',
                           "id": '04',
                           "level": 1,
                           "pictures": None,
                           "monster": True,  # 怪物
                           "book": True,  # 阅读物收集
                           "puzzle": True,  # 解密
                           "treasure": True,  # 宝箱
                           "sub_maps_id": ['0401', '0402', '0403', '0404', '0405', '0406',
                                           '0407', '0408', '0409', '0410', '0411', '0412'],
                           "layer": None,
                           },

                    }

star_rail_map = {"0001": {"name_zh": '派对车厢',
                          "parent_map_name_zh": '星穹列车',
                          "id": '0001',
                          "level": 2,
                          "pictures": None,
                          "monster": False,  # 怪物
                          "book": True,  # 阅读物收集
                          "puzzle": True,  # 解密
                          "treasure": True,  # 宝箱
                          "sub_maps_id": None,
                          "layer": {"2": {"pictures": None,
                                          "monster": False,
                                          "book": True,
                                          "puzzle": True,
                                          "treasure": True,
                                          "sub_maps_id": None, },

                                    "1": {"pictures": None,
                                          "monster": False,
                                          "book": True,
                                          "puzzle": True,
                                          "treasure": True,
                                          "sub_maps_id": None, },

                                    },
                          },

                 "0002": {"name_zh": '观景车厢',
                          "parent_map_name_zh": '星穹列车',
                          "id": '0002',
                          "level": 2,
                          "pictures": None,
                          "monster": False,  # 怪物
                          "book": True,  # 阅读物收集
                          "puzzle": True,  # 解密
                          "treasure": True,  # 宝箱
                          "sub_maps_id": None,
                          "layer": None,
                          },

                 "0003": {"name_zh": '客房车厢',
                          "parent_map_name_zh": '星穹列车',
                          "id": '0003',
                          "level": 2,
                          "pictures": None,
                          "monster": False,  # 怪物
                          "book": True,  # 阅读物收集
                          "puzzle": True,  # 解密
                          "treasure": True,  # 宝箱
                          "sub_maps_id": None,
                          "layer": None,
                          },

                 }

map01 = {"0101": {"name_zh": '主控舱段',
                  "parent_map_name_zh": '空间站黑塔',
                  "id": '0101',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0102": {"name_zh": '基座舱段',
                  "parent_map_name_zh": '空间站黑塔',
                  "id": '0102',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0103": {"name_zh": '收容舱段',
                  "parent_map_name_zh": '空间站黑塔',
                  "id": '0103',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "-1": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            },
                  },

         "0104": {"name_zh": '支援舱段',
                  "parent_map_name_zh": '空间站黑塔',
                  "id": '0104',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0105": {"name_zh": '禁闭舱段',
                  "parent_map_name_zh": '空间站黑塔',
                  "id": '0105',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         }

map02 = {"0201": {"name_zh": '行政区',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0201',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "-1": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            },
                  },

         "0202": {"name_zh": '城郊雪原',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0202',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0203": {"name_zh": '边缘通路',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0203',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0204": {"name_zh": '铁卫禁区',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0204',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0205": {"name_zh": '残响回廊',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0205',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0206": {"name_zh": '永冬岭',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0206',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0207": {"name_zh": '造物之柱',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0207',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0208": {"name_zh": '旧武器试验场',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0208',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0209": {"name_zh": '磐岩镇',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0209',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0210": {"name_zh": '大矿区',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0210',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0211": {"name_zh": '铆钉镇',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0211',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0212": {"name_zh": '机械聚落',
                  "parent_map_name_zh": '雅利洛',
                  "id": '0212',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         }

map03 = {"0301": {"name_zh": '星槎海中枢',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0301',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0302": {"name_zh": '流云渡',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0302',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0303": {"name_zh": '迴星港',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0303',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0304": {"name_zh": '长乐天',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0304',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0305": {"name_zh": '金人巷',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0305',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0306": {"name_zh": '太卜司',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0306',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0307": {"name_zh": '工造司',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0307',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0308": {"name_zh": '绥园',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0308',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0309": {"name_zh": '丹鼎司',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0309',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0310": {"name_zh": '鳞渊境',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0310',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0311": {"name_zh": '幽囚狱',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0311',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "-1": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            "-2": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            "-3": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            "-4": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            },
                  },

         "0312": {"name_zh": '竞锋舰',
                  "parent_map_name_zh": '仙舟罗浮',
                  "id": '0312',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         }

map04 = {"0401": {"name_zh": '白日梦酒店现实',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0401',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0402": {"name_zh": '黄金的时刻',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0402',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0403": {"name_zh": '筑梦边境',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0403',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0404": {"name_zh": '稚子的梦',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0404',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0405": {"name_zh": '白日梦酒店梦境',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0405',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0406": {"name_zh": '朝露公馆',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0406',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0407": {"name_zh": '克劳可影视乐园',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0407',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0408": {"name_zh": '流梦礁',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0408',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         "0409": {"name_zh": '苏乐达热砂海选会场',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0409',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0410": {"name_zh": '匹诺康尼大剧院',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0410',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": None,
                  },

         "0411": {"name_zh": '晖长石号',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0411',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "-1": {"pictures": None,
                                   "monster": False,
                                   "book": True,
                                   "puzzle": True,
                                   "treasure": True,
                                   "sub_maps_id": None, },

                            },
                  },

         "0412": {"name_zh": '匹诺康尼折纸大学学院',
                  "parent_map_name_zh": '匹诺康尼',
                  "id": '0412',
                  "level": 2,
                  "pictures": None,
                  "monster": True,  # 怪物
                  "book": True,  # 阅读物收集
                  "puzzle": True,  # 解密
                  "treasure": True,  # 宝箱
                  "sub_maps_id": None,
                  "layer": {"3": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "2": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            "1": {"pictures": None,
                                  "monster": False,
                                  "book": True,
                                  "puzzle": True,
                                  "treasure": True,
                                  "sub_maps_id": None, },

                            },
                  },

         }


def end_sign():
    pass


if __name__ == '__main__':
    files_info = [(config, r'cfg\config.json'),
                  (zh, r'cfg\language\zh.json'),
                  (en, r'cfg\language\en.json'),
                  (star_orbital_map, r'cfg\maps\data\star_orbital_map.json'),
                  (star_rail_map, r'cfg\maps\data\star_rail_map.json'),
                  (map01, r'cfg\maps\data\map01.json'),
                  (map02, r'cfg\maps\data\map02.json'),
                  (map03, r'cfg\maps\data\map03.json'),
                  (map04, r'cfg\maps\data\map04.json'),

                  ]

    for file, path in files_info:
        utils.save_json_file(path, file)

    # for key in star_orbital_map:
    #     print(key)
    #     print(type(key))
