#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import json

import requests
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'

    params = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'60',#从库中的第几部电影去取
        'limit':'20',#一次取出的个数
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }

    response = requests.get(url=url,headers=headers,params=params)
    list_data = response.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)