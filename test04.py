import tkinter as tk
from tkinter import ttk


class NavigationPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("导航目录")
        self.nodes = {}  # 存储节点结构：{id: {"var": var, "children": [], "parent": id}}

        # 创建滚动区域
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.frame = ttk.Frame(self.canvas)

        # 配置滚动区域
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", self.on_frame_configure)

        # 添加示例数据
        self.add_demo_data()

    def on_frame_configure(self, event):
        """更新滚动区域"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_node(self, parent_id, text, depth=0):
        """创建带缩进的Checkbutton节点"""
        var = tk.BooleanVar()
        cb = ttk.Checkbutton(
            self.frame,
            text=text,
            variable=var,
            command=lambda: self.on_check(var, parent_id))

        # 记录节点关系
        node_id = id(cb)
        self.nodes[node_id] = {
            "var": var,
            "children": [],
            "parent": parent_id,
            "depth": depth
        }

        # 更新父节点的子节点列表
        if parent_id in self.nodes:
            self.nodes[parent_id]["children"].append(node_id)

        # 设置缩进并打包
        cb.pack(anchor="w", padx=20 * depth, pady=2)
        return node_id

    def add_demo_data(self):
        """创建示例文档结构"""
        # 第一章
        c1 = self.create_node(None, "第一章 引言", 0)
        self.create_node(c1, "1.1 研究背景", 1)
        c1_2 = self.create_node(c1, "1.2 研究目的", 1)
        self.create_node(c1_2, "1.2.1 子目标1", 2)
        self.create_node(c1_2, "1.2.2 子目标2", 2)

        # 第二章
        c2 = self.create_node(None, "第二章 方法", 0)
        self.create_node(c2, "2.1 实验设计", 1)

    def on_check(self, current_var, parent_id):
        """处理Checkbutton状态变化"""
        current_state = current_var.get()
        node_id = [k for k, v in self.nodes.items() if v["var"] is current_var][0]

        # 更新所有子节点
        self.update_children(node_id, current_state)

        # 更新父节点状态
        if parent_id is not None:
            self.update_parent(parent_id)

    def update_children(self, node_id, state):
        """递归更新子节点状态"""
        for child_id in self.nodes[node_id]["children"]:
            self.nodes[child_id]["var"].set(state)
            self.update_children(child_id, state)

    def update_parent(self, node_id):
        """更新父节点状态"""
        parent_id = self.nodes[node_id]["parent"]
        if parent_id is None:
            return

        children_states = [
            self.nodes[child_id]["var"].get()
            for child_id in self.nodes[parent_id]["children"]
        ]

        # 如果所有子节点选中则父节点自动选中
        new_state = all(children_states)
        self.nodes[parent_id]["var"].set(new_state)

        # 继续向上递归更新
        self.update_parent(parent_id)


if __name__ == "__main__":
    root = tk.Tk()
    app = NavigationPanel(root)
    root.geometry("300x400")
    root.mainloop()