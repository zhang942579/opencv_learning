import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
word = input('请输入：')

qwe = {
    'kw': word
}
ponper = requests.post(url=url, data=qwe, headers=headers)
bun = ponper.json()
jk = f'./wangye/{word}.json'
fp = open(jk, 'w', encoding='utf-8')

json.dump(bun, fp=fp, ensure_ascii=False)

print('完成')








