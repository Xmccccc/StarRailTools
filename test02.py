class IntfBase:
    """界面基类"""

    def __init__(self, id: str, available: bool, name: str, sign_img_path: str):
        self.id = id
        self.available = available  # 是否废弃 - 活动界面等
        self.name = name
        self.sign_img_path = sign_img_path


# 假设的字典数据
intf = [{'available': True,
         'id': '01',
         'name': 'phone',
         'sign_img_path': r'cfg\pictures\zh\intf\intf01.png',
         },

        {'available': False,
         'id': '02',
         'name': 'stop',
         'sign_img_path': r'cfg\pictures\zh\intf\intf02.png',
         },
        ]

# 实例化列表
instances = []

# 根据字典创建实例并添加到列表
# for key, value in intf:
#     # 使用字典中的数据初始化类实例
#     instance = IntfBase(id=value['id'],
#                         available=value['available'],
#                         name=value['name'],
#                         sign_img_path=value['sign_img_path'])
#     instances.append(instance)
#
# # 打印结果，查看所有实例的属性
# for instance in instances:
#     print(f'ID: {instance.id}, Available: {instance.available}, Name: {instance.name}, Sign Image Path: {instance.sign_img_path}')
#
# print()
# print(instances[0].id)
# print()
# print(instances[1])

import tools

print('000')
intf01 = tools.IntfBase(intf[0])
for key, value in intf01.__dict__.items():
    print(f"{key}: {value}")
