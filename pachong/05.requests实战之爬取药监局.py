import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    url = 'https://anqiu.58.com/ershoufang/'
    page_text = requests.get(url = url,headers = headers).text
    with open('58.txt','w',encoding='utf-8') as fp:
        fp.write(page_text)
