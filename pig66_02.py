import requests
import lxml
from lxml import etree
import re

f = open('pig66.txt','r')

while True:
    n=f.readline()
    url=re.findall("http.*?html",n)
    print(url[0])
    # 打开任务页，提取数据
    ab=requests.get(url[0])
    ab.encoding = 'gbk'
    page_s = etree.HTML(ab.text)
    title = page_s.xpath('//*[@id="title"]//text()')
    con = page_s.xpath('//*[@id="article"]/p//text()')

    # 组装文本地址
    root_d = "C:\\Users\\Administrator\\Desktop\\pig66\\"
    pic = root_d + title[0]+'.txt'
    l = open(pic, 'a', encoding='utf-8')

    for t in title:
        l.write(t)
        l.write('\n')
        print(t)
    for i in con:
        l.write(i)
        l.write('\n')
    l.close()
