# -*- coding:utf-8 -*-

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
print(f"Status code: {r.status_code}")
# 将API存储在一个变量中
response_dict = r.json()
# 处理结果
print(f"总共多少： {response_dict['total_count']}")
repo_dicts = response_dict['items']

print('Number of items:', len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'] # 相当与打开相应的github页面
    }
    plot_dicts.append(plot_dict)
# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('../statics/python_repos2_javascript.svg')




# ////////////////////////////////

# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 可视化
# my_style = LS('#333366', base_style=LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
# chart.add('', stars)
# chart.render_to_file('../statics/python_repos.svg')

# /////////////////////////////////

# ====================================
# print(f"Repositories returned: ", len(repo_dicts))
# 第一个仓库
# repo_dict = repo_dicts[1]
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# =====================================