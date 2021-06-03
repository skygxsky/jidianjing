# -*- coding: utf-8 -*-
'''

'''


import execjs
import time
import requests




payload = "{\"site\":[\"jdj&365\",\"jdj007\"]}"
headers = {
  'authority': 'www.jdj007.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'accept': 'application/json, text/plain, */*',
  'x-requested-with': 'XMLHttpRequest',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://www.jdj007.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.jdj007.com/',
  'accept-language': 'zh,zh-CN;q=0.9',
}

timestamp = int(time.time()*1000)

str1 = "timestamp=" + str(timestamp) + "&secret=aHVheWluZ19zZWNyZXRfYXBp"

js = open('get_sign.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(js)
sign = ctx.call('getSign',str1)

print(sign)
url = f"https://www.jdj007.com/api/article/type?timestamp={timestamp}&sign={sign}"

response = requests.post(url, headers=headers, data = payload)

print(response.text)

