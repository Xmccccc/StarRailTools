import tkinter as tk


class FrameTools(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "功能"
        self.parent = parent
        # button
        tk.Button(self, text="锄地", command=lambda: self.show_frame_callback("FrameMapClean"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=0, column=0, padx=50, pady=50)
        tk.Button(self, text="剧情", command=lambda: print("1"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=0, column=1, padx=50, pady=50)
        tk.Button(self, text="模拟宇宙", command=lambda: print("2"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=0, column=2, padx=50, pady=50)
        tk.Button(self, text="忘却之庭", command=lambda: print("3"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=0, column=3, padx=50, pady=50)

        tk.Button(self, text="全部执行", command=lambda: print("4"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=1, column=0, padx=50, pady=50)
        tk.Button(self, text="选择执行", command=lambda: print("5"),
                  width=8, height=1, font=('Georgia', 14)).grid(row=1, column=1, padx=50, pady=50)

        # label
        # label01 = tk.Label(self, text="功能界面", font=('Georgia', 14))
        # label01.grid()

    def show_frame_callback(self, frame_name):
        self.parent.show_frame(frame_name)


class FrameTheme(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "主题"
        # button
        button01 = tk.Button(self, text="主题")
        button01.pack()

        # label
        label01 = tk.Label(self, text="主题界面")
        label01.pack()


class FrameSetting(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "设置"
        # button
        button01 = tk.Button(self, text="设置")
        button01.pack()

        # label
        label01 = tk.Label(self, text="设置界面")
        label01.pack()


class FrameAbout(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "关于"
        # button
        button01 = tk.Button(self, text="关于")
        button01.pack()

        # label
        label01 = tk.Label(self, text="关于界面")
        label01.pack()


class FrameCleanMonster(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = "锄地设置界面"
        # label
        tk.Label(self, text="地图选择", font=('Georgia', 14)).grid(row=0, column=0, padx=20, pady=10)
        # button
        tk.Button(self, text="锄地").grid(row=1, column=0, padx=20, pady=10)


left_button_dict = {"FrameTools": FrameTools,
                    "FrameTheme": FrameTheme,
                    "FrameSetting": FrameSetting,
                    "FrameAbout": FrameAbout,
                    }

frames_dict = {"FrameTools": FrameTools,
               "FrameTheme": FrameTheme,
               "FrameSetting": FrameSetting,
               "FrameAbout": FrameAbout,
               "FrameMapClean": FrameCleanMonster,
               }
