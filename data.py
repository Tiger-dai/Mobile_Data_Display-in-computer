import csv

CSV_FILE = "fund_flow_data.csv"

def init_csv():
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            header = f.readline().strip()
            if header != "采集时间,大盘资金净流入(亿)":
                raise FileNotFoundError
    except FileNotFoundError:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["采集时间", "大盘资金净流入(亿)"])
        print("✅ 已创建CSV数据文件")

def append_to_csv(time_str, value):
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([time_str, round(value, 2)])
