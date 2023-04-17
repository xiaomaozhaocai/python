#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#分页爬取
import os.path

import requests
import re

if __name__ == '__main__':

    if not os.path.exists('./gaoxiao'):
        os.mkdir('./gaoxiao')

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    
    url = 'https://www.gaoxiaojob.com/announcement/detail/95348.html'
    for pageNum in range(1, 36):
        newUrl = format(url % pageNum)

        page_text = requests.get(url=newUrl, headers=headers).text

        with open('./gaoxiao/1.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)

        ex = '<div class="detail-item">.*?<li class="el-col">(.*?)</li>'
        img_src_list = re.findall(ex, page_text, re.S)
        for oneList in img_src_list:
            src = 'https:' + oneList
            img_data = requests.get(url=src, headers=headers).content
            img_name = src.split('/')[-1]
            imgPath = './qiuTuLibs/'+img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)

