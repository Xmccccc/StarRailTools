import tkinter as tk
import sys


def draw_hollow_box(x, y, width, height, border_color='red', border_width=2):
    """
    在屏幕上绘制一个空心方框
    :param x: 方框左上角x坐标
    :param y: 方框左上角y坐标
    :param width: 边框宽度
    :param height: 边框高度
    :param border_color: 边框颜色（默认红色）
    :param border_width: 边框线条宽度（默认2像素）
    :return:
    """
    root = tk.Tk()
    root.overrideredirect(True)  # 移除窗口装饰
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.attributes('-topmost', True)  # 窗口置顶
    root.attributes('-transparentcolor', 'white')  # 白色透明

    # 设置鼠标事件穿透（Windows系统）
    if sys.platform == 'win32':
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
            ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
            ex_style |= 0x00000020  # WS_EX_TRANSPARENT
            ex_style |= 0x00080000  # WS_EX_LAYERED
            ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style)
        except Exception as e:
            print("鼠标穿透设置失败:", e)

    # 创建画布并绘制边框
    canvas = tk.Canvas(root, bg='white', highlightthickness=0)
    canvas.create_rectangle(
        0,
        0,
        width - 1,  # 避免边框被裁剪
        height - 1,
        outline=border_color,
        width=border_width
    )
    canvas.pack(fill='both', expand=True)

    root.mainloop()


# 使用示例：在屏幕(100,100)位置绘制200x150的红色方框
if __name__ == "__main__":
    draw_hollow_box(100, 100, 200, 150)
