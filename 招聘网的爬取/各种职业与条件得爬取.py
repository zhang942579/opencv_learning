import requests
from lxml import etree
import pymysql
url = 'https://login.51job.com/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
data = {
    'lang': 'c',
    'action': 'save',
    'from_domain': 'i',
    'with_geetest': 'yes',
    'geetest_challenge': '6579b645a1e90a937cd26afaf7ecf721',
    'geetest_validate': '869c2353e415ae584227e33ca4c48d7f',
    'geetest_seccode': '869c2353e415ae584227e33ca4c48d7f|jordan',
    'loginname_encrypt': 'S5d44P7Cp4pYat+WsQ9Xhw==',
    'password_encrypt': 'DMUE4y0AqBUdIKbqFm2GcA=='
}
session = requests.Session()
resp = session.post(url=url, headers=headers, data=data)
# ch = resp.content.decode('GBK')
# with open('./templates/zhuye.html', 'w', encoding='gbk')as f:
#     f.write(ch)
#所有职业名称和链接的爬取，并存储在列表中
position_url = 'https://jobs.51job.com/'
position_resp = session.get(url=position_url, headers=headers).text.encode('iso-8859-1').decode('gbk')
position_tree = etree.HTML(position_resp)
position = position_tree.xpath('//div[@class="e e5"]')
all_position = []
all_link = []
for a in position:
    positions = a.xpath('./div[1]/a')
    for b in positions:
        positionss = b.xpath('./text()')[0]
        all_position.append(positionss)
        links = b.xpath('./@href')[0]
        all_link.append(links)
print(all_position, len(all_position))
# print(all_link, len(all_link))
#for c in all_link:
link_url = all_link[0]
link_resp = session.get(url=link_url, headers=headers).text.encode('iso-8859-1').decode('gbk')
link_tree = etree.HTML(link_resp)
link_requirement = link_tree.xpath('//div[@class="e "]/p[2]/text()')
link_position = link_tree.xpath('//div[@class="e "]/p/span/a/text()')
print(link_requirement, len(link_requirement))
print(link_position, len(link_position))


conn = pymysql.connect(host='D:/software_code/mySQL/phpstudy_pro/Extensions/MySQL5.7.26/data/', user='root', password='zhang123', database='test', charset='utf8')





