import requests
import time
import lxml
from lxml import etree





w=open("ali02.txt","a")
# 打开文本，循环读取店铺地址
f=open("ali01.txt","r",encoding='utf-8')
while True:
    m=f.readline()


        # 请求地址并转码
    page=requests.get(m)
    page_sour=etree.HTML(page.text)

    #     开始获取“联系方式”

    newurl=page_sour.xpath('//*[@id="topnav"]/div/ul/li[6]/a//@href')
    for i in newurl:
        w.write(i)
        w.write("\n")






