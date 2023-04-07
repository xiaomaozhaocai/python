#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#需求爬取搜狗首页数据

import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    url = 'https://piccdn3.umiwi.com/img/202303/22/202303221607377926894791.jpeg'

    img_data = requests.get(url=url,headers=headers).content

    with open('tupian.jpeg','wb') as fp:
        fp.write(img_data)

