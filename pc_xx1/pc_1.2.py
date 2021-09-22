
import requests

url = 'http://www.sogou.com/'
re = requests.get(url=url)
ra = re.text
dz = './wangye/sogou.html'
with open(dz, 'w', encoding='utf-8')as f:
    f.write(ra)
