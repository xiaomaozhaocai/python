#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':

    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }
    page_text = requests.get(url=url,headers=headers).text
    with open('./huazhuangpin.html','w',encoding='utf-8') as fp:
        fp.write(page_text)


