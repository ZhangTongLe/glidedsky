#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/9 16:44
# @Author : way
# @Site : 
# @Describe: 用于更新 md 索引

md = """# glidedsky
glidedsky 爬虫练习笔记

# note

- 爬虫采集属于 io 密集型操作，使用多线程并发可以提高效率，但是最佳并发数取决于爬虫的机器配置，而不是越多越好
- 网络请求有时候会出错，重试是必要的，不用框架的话，装饰器是很好的选择
- 使用代理 ip 时，网络错误导致漏爬的可能性很高，只有重试是不够的，先把结果存下来，做好补爬的准备，是比较稳妥的策略

## list
| 代码 | 说明  | 
| ------------ | ------------ |
"""

import re
import os

for demo in os.listdir():
    if demo.startswith('crawler') and demo.endswith('py'):
        with open(demo, 'r', encoding='utf-8') as f:
            desc = re.findall("@Describe:(.*)", f.read())
        desc = desc[0].strip() if desc else ''
        str = f"| [{demo}](https://github.com/TurboWay/glidedsky/blob/master/{demo})       | {desc} |\n"
        md += str

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(md)