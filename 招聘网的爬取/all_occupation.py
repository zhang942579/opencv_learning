import requests
from lxml import etree


headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
}
url = 'https://jobs.zhaopin.com/'


page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
div_list = tree.xpath('/html/body/div/div[3]/div[1]/div[3]/div/div[3]/div[1]/div[2]/a[1]')
a_occupations = []
#for a in div_list:
    #a_occupation = a.xpath('./a/text()')[0]
a_occupations.append(div_list)

print(a_occupations)






