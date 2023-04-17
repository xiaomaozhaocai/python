#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os.path
from bs4 import BeautifulSoup
import lxml
import requests
import re

if __name__ == '__main__':

    if not os.path.exists('./sanGuoYanYi'):
        os.mkdir('./sanGuoYanYi')

    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    page_text = requests.get(url=url, headers=headers).text

    # 解析标题和详情文本内容
    # 1.实例化BeautifulSoup对象，需要将页面源码加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanGuoYanYi/sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        titleName = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # print(titleName)

        detail_page_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.select('.chapter_content')
        content = div_tag[0].text
        print(content)

        fp.write(titleName + ':' + content + '\n')
        print(titleName,'爬取成功')

        break

