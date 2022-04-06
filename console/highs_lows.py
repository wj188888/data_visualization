# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import matplotlib
import pandas_profiling


print(matplotlib.get_backend())
matplotlib.use('module://backend_interagg')
filename = '../statics/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    for row in enumerate(header_row):
        highs.append(row[1])
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()