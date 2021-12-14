import json

import requests

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'

    word = input('please enter a word:')

    data = {
        'kw':word
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'
    }
    reponse = requests.post(url=post_url,data=data,headers=headers)

    #json方法返回的是一个obj（如果确认响应数据是json数据，才可以使用）
    page_json = reponse.json()

    #持久化存储
    fp = open('./dog.json','w',encoding='utf-8')
    json.dump(page_json,fp=fp,ensure_ascii=False)

    print(fp)
