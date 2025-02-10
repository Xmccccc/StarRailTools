# utils 基础组件 - 可通用
import json


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


