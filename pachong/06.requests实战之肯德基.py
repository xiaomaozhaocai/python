import json
import requests

if __name__ == '__main__':
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    word = input("请输入地址: ")
    data = {
            'cname': '',
            'pid': '',
            'keyword': word,
            'pageIndex': 1,
            'pageSize': '10',
        }
    response = requests.post(url=url, data=data, headers=header)
    text_list = response.json()
    fp = open('./kdj.json', 'w', encoding='utf-8')
    json.dump(text_list, fp=fp, ensure_ascii=False)

