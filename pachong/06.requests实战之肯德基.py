import json
import requests

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
word = input("请输入地址: ")
numbers = 1
# 页数
number_pages = 0
# 第一次检测页数
state = True

data = {
        'cname': '',
        'pid': '',
        'keyword': word,
        'pageIndex': 1,
        'pageSize': '10',
    }

# while numbers != 0:
#     number_pages += 1


response = requests.post(url=url, data=data, headers=header)

# print(response)
#
# exit()

text_list = response.json()

fp = open('./kdj.json', 'w', encoding='utf-8')
json.dump(text_list, fp=fp, ensure_ascii=False)

#
# numbers -= 1
# # 计算页数,因为只需要一次即可
# if state:
#     # 将列表text转化为字典
#     dictionary = eval(text)
#     # 获取第一段Table的页数
#     rowcount = dictionary['Table']
#     # 将这个列表中的字典赋给dicts
#     dicts = rowcount[0]
#     # 查询rowcount所指的页数
#     numbers = dicts['rowcount']
#     if numbers == 0:
#         print("抱歉,您所输入的地址没有肯德基餐厅")
#     else:
#         print(f"{word}一共有{numbers}家肯德基餐厅")
#     if numbers % 10 == 0:
#         numbers = numbers // 10
#     else:
#         numbers = numbers // 10  # 不加一是因为已经检查过一次了
#     state = False
#
# print(text)