# -*- coding:utf-8 -*-

import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f"Status code: {r.status_code}")
# 将API存储在一个变量中
response_dict = r.json()
# 处理结果
print(f"总共多少： {response_dict['total_count']}")
repo_dicts = response_dict['items']
print(f"Repositories returned: ", len(repo_dicts))
# 第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)