import requests
import json
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
}
dizhi = input('输入地址:')
yemian = input('第几页：')

data = {
    'cname': '',
    'pid': '',
    'keyword': dizhi,
    'pageIndex': yemian,
    'pageSize': '10'
}

pongere = requests.post(url=url, data=data, headers=headers)
zxc = pongere.text
jk = f'./wangye/{dizhi}.json'
with open(jk, 'w', encoding='utf-8')as f:
    f.write(json.dumps(zxc, ensure_ascii=False))














