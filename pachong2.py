from urllib import request, parse

data = bytes(parse.urlencode({'word':'hello'}),encoding='utf-8')
# print(data)

response = request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get',timeout=1)
print(response2.read().decode('utf-8'))

import socket
import urllib

try:
    response3 = request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('timeout')

# print(response2.read().decode('utf-8'))
