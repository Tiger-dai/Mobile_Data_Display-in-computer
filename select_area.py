import tkinter as tk
import re

class ROISelector:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

        self.canvas = tk.Canvas(root, cursor="cross", bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.rect = None
        self.roi = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y,
            self.start_x, self.start_y,
            outline="red", width=2
        )

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)
        self.roi = (x1, y1, x2, y2)
        self.root.destroy()

def update_config(roi):
    with open("config.py", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r"SCREEN_REGION = \(\d+, \d+, \d+, \d+\)",
        f"SCREEN_REGION = {roi}",
        content
    )

    with open("config.py", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ 坐标已自动保存：{roi}")

def get_region():
    root = tk.Tk()
    app = ROISelector(root)
    root.mainloop()
    return app.roi

if __name__ == "__main__":
    print("请框选需要识别的数字区域，松开鼠标完成…")
    region = get_region()
    if region:
        update_config(region)
        print("✅ 配置完成，现在可以运行 main.py 开始采集")
    else:
        print("❌ 未选择区域")