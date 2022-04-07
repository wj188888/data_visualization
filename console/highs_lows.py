# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import matplotlib
# import pandas_profiling
from datetime import datetime

# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)

# print(matplotlib.get_backend())
# matplotlib.use('module://backend_interagg')
filename = '../statics/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

