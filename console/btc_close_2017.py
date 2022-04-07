# -*- coding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    from urllib.request import urlopen
except ImportError:
    # python 2.x版本
    from urllib2 import urlopen
import json

def load_jsondata():
    json_url = r'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    response = urlopen(json_url)
    # 读取数据
    req = response.read()
    # 将数据写入文件
    with open('../statics/btc_close_2017_urllib.json', 'wb') as f:
        f.write(req)
    # 加载json格式
    # file_urllib = json.loads(req)

def read_jsondata():
    """加载json数据"""
    # 创建5个列表，分别存储日期和收盘价
    dates, months, weeks, weekdays, closes = [], [], [], [], []

    filename = r'../statics/btc_close_2017_urllib.json'
    with open(filename) as f:
        btc_data = json.load(f)
    # 打印每一天的信息
    for btc_dict in btc_data:
        dates.append(btc_dict['date'])
        months.append(int(btc_dict['month']))
        weeks.append(int(btc_dict['week']))
        weekdays.append(btc_dict['weekday'])
        closes.append(int(float(btc_dict['close'])))
    return dates, closes, months, weeks, weekdays

def show_chart():
    """图标展示"""
    import pygal
    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=True)
    line_chart.title = '收盘价($)'
    dates, close, *other= read_jsondata()
    line_chart.x_labels = dates
    N = 50
    line_chart._x_labels_major= dates[::N]
    print(line_chart._x_labels_major)
    line_chart.add('收盘价', close)
    line_chart.render_to_file('../statics/收盘价折线图($).svg')


def draw_line(x_data, y_data, title, y_legend):
    """收盘均值价"""
    from itertools import groupby
    import pygal

    xy_map =[]
    for x,y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _,v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(f'../statics/{title}.svg')
    return line_chart

if __name__ == '__main__':
    dates, closes, months, weeks, weekdays = read_jsondata()
    idx_month = dates.index('2017-12-01')
    idx_week = dates.index('2017-12-11')
    wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
          'Friday', 'Saturday', 'Sunday']
    weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
    line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week],
                                   '收盘价星期均值($)', '星期均值')
    line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五',
                                   '周六', '周天']
    line_chart_month = draw_line(months[:idx_month], closes[:idx_month],
                                 '收盘价月日均值($)', '月日均值')
    line_chart_week = draw_line(weeks[1: idx_week], closes[1:idx_week],
                                '收盘价周日均值($)', '周日均值')


    # 将这些图表放在一个数据仪表盘里：
    with open('../statics/收盘价DashBoard.html', 'w', encoding='utf-8') as html_file:
        html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
        for svg in ['收盘价月日均值($).svg', '收盘价周日均值($).svg', '收盘价星期均值($).svg',
                    '收盘价星期均值.svg']:
            html_file.write(f'<object type="image/svg+xml" data="{svg}" height=500></object>\n')
        html_file.write('</body></html>')