import tkinter as tk
from tkinter import ttk

# 定义常量，用于表示选中与未选中状态
CHECKED = "☑"
UNCHECKED = "☐"


class NavigationPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("导航目录")

        # 设置字体大小和样式
        self.set_style()

        # 创建Treeview组件
        self.tree = ttk.Treeview(
            self.root,
            columns=("status",),
            show="tree headings",
            selectmode="none"
        )

        # 配置列参数
        self.tree.heading("#0", text="文档结构")
        self.tree.heading("status", text="状态")
        self.tree.column("#0", width=200, stretch=True)
        self.tree.column("status", width=60, anchor="center")

        # 添加示例数据
        self.add_demo_data()

        # 绑定点击事件
        self.tree.bind("<Button-1>", self.on_click)

        # 使用grid布局，可以后续灵活布局其他组件
        self.tree.grid(row=0, column=0, sticky="nsew")

        # 配置窗口的grid布局管理
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def set_style(self):
        """设置字体大小和样式"""
        style = ttk.Style()

        # 设置字体大小和树形结构文本的样式
        style.configure("Treeview",
                        font=("Arial", 12))  # 设置字体为Arial，大小为12

        # 设置表头字体和颜色
        style.configure("Treeview.Heading",
                        font=("Arial", 14, "bold"),  # 设置表头字体为加粗14号字体
                        foreground="blue")  # 设置表头文字颜色为蓝色

    def add_demo_data(self):
        """添加测试数据，展示文档结构的树形层级"""
        chapter1 = self.tree.insert("", "end", text="第一章 引言", values=(UNCHECKED,))
        self.tree.insert(chapter1, "end", text="1.1 研究背景", values=(UNCHECKED,))
        sub_section = self.tree.insert(chapter1, "end", text="1.2 研究目的", values=(UNCHECKED,))
        self.tree.insert(sub_section, "end", text="1.2.1 子目标1", values=(UNCHECKED,))
        self.tree.insert(sub_section, "end", text="1.2.2 子目标2", values=(UNCHECKED,))

        chapter2 = self.tree.insert("", "end", text="第二章 方法", values=(UNCHECKED,))
        self.tree.insert(chapter2, "end", text="2.1 实验设计", values=(UNCHECKED,))

    def on_click(self, event):
        """处理点击事件，切换选中与未选中状态"""
        region = self.tree.identify("region", event.x, event.y)
        column = self.tree.identify_column(event.x)
        item = self.tree.identify_row(event.y)

        # 检查点击的是有效的项
        if item:
            current_value = self.tree.item(item, "values")[0]
            new_value = CHECKED if current_value == UNCHECKED else UNCHECKED
            self.tree.item(item, values=(new_value,))

            # 判断是否是父节点，如果是父节点，更新所有子节点状态
            if self.tree.get_children(item):
                self.update_children_state(item, new_value)
                self.update_parent_state(item)

            # 输出状态变更日志
            node_type = "父节点" if self.tree.get_children(item) else "子节点"
            print(f"{node_type} [{self.tree.item(item, 'text')}] 状态变为 {new_value}")

    def update_children_state(self, parent, state):
        """递归更新所有子节点的状态"""
        for child in self.tree.get_children(parent):
            self.tree.item(child, values=(state,))
            # 如果子节点有子节点，递归更新
            if self.tree.get_children(child):
                self.update_children_state(child, state)

    def update_parent_state(self, parent):
        """检查并更新父节点状态，若所有子节点都选中，父节点选中"""
        children = self.tree.get_children(parent)
        if all(self.tree.item(child, "values")[0] == CHECKED for child in children):
            self.tree.item(parent, values=(CHECKED,))
        else:
            self.tree.item(parent, values=(UNCHECKED,))


if __name__ == "__main__":
    root = tk.Tk()
    app = NavigationPanel(root)
    root.geometry("300x400")
    root.mainloop()
