#!usr/bin/env python3
#-*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }

    #指定url
    url = 'https://www.sogou.com/web?'
    #处理url所携带的url参数
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #发起请求
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,'保存成功了')
