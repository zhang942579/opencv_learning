import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
a_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
id_list = []#存储id列表
all_list = []#存储所有的列表
for page in range(1, 5):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }

    a_qq = requests.post(url=a_url, headers=headers, data=data).json()
    for dic in a_qq['list']:
        id_list.append(dic['ID'])

b_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

for id in id_list:
    data = {
        'id': id
    }
    b_qq = requests.post(url=b_url, headers=headers, data=data).json()
    all_list.append(b_qq)
fp = open('./wangye/hzyj.json', 'w', encoding='utf-8')
json.dump(all_list, fp=fp, ensure_ascii=False)












