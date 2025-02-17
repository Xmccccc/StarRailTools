import tkinter as tk
from tkinter import ttk


class TreeviewExample(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(sticky="nsew")

        # 创建 Treeview
        self.tree = ttk.Treeview(self, columns=("Name", "Age"))
        self.tree.grid(row=1, column=0, sticky="nsew")  # 使用 grid 布局

        # 设置列头
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Age")

        # 添加示例数据
        self.tree.insert('', 'end', text="John", values=("John", "28"))
        self.tree.insert('', 'end', text="Alice", values=("Alice", "30"))
        self.tree.insert('', 'end', text="Bob", values=("Bob", "25"))

        # 设置字体和行高
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Arial", 16), rowheight=30)

        # 设置表头样式
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        # 设置默认背景颜色
        self.default_bg = self.tree.tag_configure("default", background="white")
        self.hover_bg = self.tree.tag_configure("hover", background="#e0e0e0")  # 鼠标悬停背景色

        # 绑定鼠标事件
        self.tree.bind("<Motion>", self.on_mouse_move)
        self.tree.bind("<Leave>", self.on_mouse_leave)

        # 用于记录鼠标悬停的项目
        self.hovered_item = None

    def on_mouse_move(self, event):
        # 获取鼠标当前所在位置对应的行
        item = self.tree.identify_row(event.y)

        # 如果没有新行被识别，直接返回
        if not item:
            return

        # 如果当前行与上次悬停的行不同，则更新背景颜色
        if item != self.hovered_item:
            # 恢复上一个悬停行的背景颜色
            if self.hovered_item:
                self.tree.item(self.hovered_item, tags="default")

            # 更新当前悬停行的背景颜色
            self.tree.item(item, tags="hover")
            self.hovered_item = item  # 更新悬停的项目

    def on_mouse_leave(self, event):
        # 鼠标离开时，恢复背景颜色
        if self.hovered_item:
            self.tree.item(self.hovered_item, tags="default")
        self.hovered_item = None


# 创建根窗口并运行
root = tk.Tk()
app = TreeviewExample(root)
root.mainloop()
