#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#需求爬取搜狗首页数据
import os.path

import requests
import re

if __name__ == '__main__':

    if not os.path.exists('./gaoxiao'):
        os.mkdir('./gaoxiao')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    url = 'http://www.gaoxiaojob.com/announcement/detail/95348.html'

    page_text = requests.get(url=url, headers=headers).text

    with open('./gaoxiao/1.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    ex = '<div class="detail-item">.*?<li class="el-col">(.*?)</li>'
    img_src_list = re.findall(ex, page_text, re.S)
    for onelist in img_src_list:
        print(onelist)

