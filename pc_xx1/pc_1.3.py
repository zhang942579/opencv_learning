import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


url = 'https://www.baidu.com/s?'

zx = input('请输入：')
cv = {
    'wd': zx
}
qwer = requests.get(url=url, params=cv, headers=headers)
zhe = qwer.text
jk = f'./wangye/{zx}.html'
with open(jk, 'w', encoding='utf-8') as f:
    f.write(zhe)
print('完成')



