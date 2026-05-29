import time
import mss
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
import easyocr

from config import SCREEN_REGION, REFRESH_RATE
import data

ALLOWED = "0123456789.-"

print("加载OCR模型...")
reader = easyocr.Reader(['en'], gpu=False, verbose=False)
print("✅ 启动成功，开始采集…\n")

def preprocess(img):
    img_gray = ImageOps.grayscale(img)
    enhancer = ImageEnhance.Contrast(img_gray)
    img_contrast = enhancer.enhance(4.0)
    img_big = img_contrast.resize((img_contrast.width*2, img_contrast.height*2))
    return np.array(img_big)

def run_detect():
    data.init_csv()
    last_valid = None

    with mss.MSS() as sct:
        monitor = {
            "left": SCREEN_REGION[0],
            "top": SCREEN_REGION[1],
            "width": SCREEN_REGION[2] - SCREEN_REGION[0],
            "height": SCREEN_REGION[3] - SCREEN_REGION[1],
        }

        while True:
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            img_np = preprocess(img)

            res = reader.readtext(
                img_np,
                allowlist=ALLOWED,
                detail=0,
                text_threshold=0.2,
                low_text=0.1
            )

            text = "".join(res).strip()
            clean = "".join([c for c in text if c in ALLOWED])
            now = time.strftime("%Y-%m-%d %H:%M:%S")

            try:
                val = float(clean)
                # 只保留小数点后2位
                val = round(val, 2)
                last_valid = val
                print(f"[{now}] {val}")
            except:
                if last_valid is not None:
                    val = last_valid
                    print(f"[{now}] 识别失败 → 使用上一次：{val}")
                else:
                    print(f"[{now}] 首次失败，跳过")
                    time.sleep(REFRESH_RATE)
                    continue

            data.append_to_csv(now, val)
            time.sleep(REFRESH_RATE)

if __name__ == "__main__":
    try:
        run_detect()
    except KeyboardInterrupt:
        print("\n🛑 已停止采集")