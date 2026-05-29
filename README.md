# 手机APP数据PC端连续展示工具
一键监控屏幕指定区域数字，自动OCR识别并保存为CSV文件

![工具演示](demo.png)
<img width="1296" height="616" alt="无标题" src="https://github.com/user-attachments/assets/4e949e67-7664-41de-892e-97c9a8736691" />

---

## 项目灵感
为了方便观察某炒股软件上的“大盘资金净流入”数据（PC版炒股软件没用）

---

## 手机投屏电脑
市场上免费的投屏工具很多，我使用的是“幕连”免费版

---

## 快速使用

1. 双击运行 `手机数据观察程序.bat`
2. 按提示框选要识别的数字区域
3. 启动采集，数据自动保存到 `fund_flow_data.csv`

---

## 安装依赖
```bash
pip install mss numpy pillow easyocr
```

---

## 功能特性
- 可视化框选识别区域
- 0.5秒高频采集（可配置）
- 图像增强 + 稳定OCR
- 识别失败自动复用上次有效值
- 实时控制台输出 + CSV持久化
- 一键批处理启动

---

## 原始配置项（config.py）
```python
SCREEN_REGION = (x1, y1, x2, y2)  # 识别区域
REFRESH_RATE = 0.5                # 采集间隔（秒）
```

---

## 核心模型（easyOCR）
Mobile_Data_Display-easyOCR_modle
由于网络和其他因素，下载easyOCR中模型经常出问题，我把模型发布出来，需要的话直接下载
下载后放到 C:\用户\Administrator\.EasyOCR\model 中即可
链接: https://pan.baidu.com/s/1qe9FBhmETAm21FJoJ6FV9Q?pwd=qeh8 提取码: qeh8 

---

## 文件说明
- main.py：主采集程序
- select_area.py：区域选择工具
- data.py：CSV数据管理
- config.py：参数配置
- 手机数据观察程序.bat：一键启动脚本

---

## 感慨
我干了20年的IT销售管理和售前顾问，事业不顺尝试自己写代码，学了3个月Python，计划用Python解决生活中遇到的实际问题
---
