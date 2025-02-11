import tkinter as tk
from tkinter import ttk


class Tools(tk.Tk):
    def __init__(self):
        super().__init__()

        # 初始化窗口
        self._init_window()

        # 创建左侧菜单
        self._create_menu()

        # 创建内容区域
        self._create_content_area()

        # 初始化其他属性
        self.position = 'none'
        self.energy = 0
        self.stored_energy = 0
        self.money = 0

    def _init_window(self):
        """初始化窗口尺寸和位置"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(True, True)
        self.title("StarRailTools v0.1")

    def _create_menu(self):
        """创建左侧菜单栏"""
        # 菜单容器
        self.menu_frame = tk.Frame(
            self,
            bg="#2d2d2d",  # 深灰背景色
            width=150,  # 固定宽度
            relief=tk.FLAT
        )
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # 菜单项配置
        menu_items = [
            {"text": "状态监控", "command": self.show_status},
            {"text": "能量管理", "command": self.show_energy},
            {"text": "金币统计", "command": self.show_money},
            {"text": "设置", "command": self.show_settings}
        ]

        # 动态创建菜单按钮
        self.menu_buttons = []
        for idx, item in enumerate(menu_items):
            btn = tk.Button(
                self.menu_frame,
                text=item["text"],
                command=item["command"],
                bg="#2d2d2d",  # 默认背景色
                fg="white",  # 文字颜色
                activebackground="#404040",  # 点击时背景色
                activeforeground="white",
                borderwidth=0,
                anchor="w",
                padx=20,
                pady=15,
                width=15
            )
            btn.pack(fill=tk.X, pady=(10 if idx == 0 else 0))
            self.menu_buttons.append(btn)

    def _create_content_area(self):
        """创建右侧内容区域"""
        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 默认显示状态页
        self.current_content = None
        self.show_status()

    # 以下是菜单功能实现示例 ------------------------------
    def _clear_content(self):
        """清空内容区域"""
        if self.current_content:
            self.current_content.destroy()

    def show_status(self):
        """显示状态页面"""
        self._clear_content()
        self.current_content = tk.Frame(self.content_frame, bg="white")
        self.current_content.pack(fill=tk.BOTH, expand=True)

        # 示例内容
        tk.Label(
            self.current_content,
            text="当前状态监控",
            font=("Arial", 16),
            bg="white"
        ).pack(pady=20)

    def show_energy(self):
        """显示能量管理页面"""
        self._clear_content()
        self.current_content = tk.Frame(self.content_frame, bg="#f0f0f0")
        self.current_content.pack(fill=tk.BOTH, expand=True)

        # 示例内容
        ttk.Label(
            self.current_content,
            text="能量管理系统",
            font=("Arial", 16)
        ).pack(pady=20)
        ttk.Progressbar(
            self.current_content,
            length=200,
            mode="determinate",
            value=45
        ).pack()

    def show_money(self):
        """显示金币统计页面"""
        self._clear_content()
        self.current_content = tk.Frame(self.content_frame, bg="#f0f0f0")
        self.current_content.pack(fill=tk.BOTH, expand=True)

        # 示例表格
        columns = ("时间", "类型", "金额")
        tree = ttk.Treeview(
            self.current_content,
            columns=columns,
            show="headings"
        )
        for col in columns:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

    def show_settings(self):
        """显示设置页面"""
        self._clear_content()
        self.current_content = tk.Frame(self.content_frame, bg="white")
        self.current_content.pack(fill=tk.BOTH, expand=True)

        # 示例设置项
        ttk.Checkbutton(
            self.current_content,
            text="自动保存设置"
        ).pack(pady=10, anchor="w")


if __name__ == "__main__":
    app = Tools()
    app.mainloop()