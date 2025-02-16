import tkinter as tk


def update_selected_list():
    selected_items = [text for text, var in check_vars if var.get() == 1]
    listbox.delete(0, tk.END)
    for item in selected_items:
        listbox.insert(tk.END, item)


# 创建主窗口
root = tk.Tk()
root.title("分页选择示例")

# 示例字符串列表
strings = [
    "苹果", "香蕉", "橙子", "葡萄", "西瓜",
    "菠萝", "芒果", "草莓", "梨子", "桃子"
]

# 存储Checkbutton的变量（文本和IntVar）
check_vars = []

# 创建Checkbutton的容器
check_frame = tk.Frame(root)
check_frame.pack(padx=10, pady=10, fill="x")

# 为每个字符串创建Checkbutton并布局
for text in strings:
    var = tk.IntVar()
    check_vars.append((text, var))

    # 创建每行的Frame容器
    row_frame = tk.Frame(check_frame)
    row_frame.pack(fill="x", pady=5)

    # 文本部分
    label = tk.Label(row_frame, text=text, anchor="w")
    label.pack(side="left", padx=10, fill="x", expand=True)

    # 勾选框部分
    cb = tk.Checkbutton(
        row_frame,
        variable=var,
        command=update_selected_list,  # 绑定更新函数
    )
    cb.pack(side="right", padx=10)

# 创建显示选中列表的Listbox
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
