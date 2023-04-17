#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 分页爬取
import os.path
from bs4 import BeautifulSoup
import lxml
import requests
import re

if __name__ == '__main__':
    fp = open('./gaoxiao/1.html', 'r', encoding='utf-8')
    # 实例化BeautifulSoup对象
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup.div)
    print(soup.select('.is-basic')[0].get_text())

    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
