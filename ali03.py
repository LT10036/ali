  #-*-coding:utf8-*-
import requests
from lxml import etree
import re





# f=open("111.txt","r",encoding='utf-8')
# a=f.read()


f=open("ali02.txt","r",encoding='utf-8')
m=open("ali03.txt","a",encoding="utf-8")

#  公司名称           //*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/h4
# 联系人              //*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/dl/dd

try:
    while True:
        n=f.readline()

        url=re.findall("http.*?htm",n)
        # 打开任务页，提取数据
        ab=requests.get(url[0])
        a=ab.text

        # 转成页面 xpath
        ab=etree.HTML(a)

        # 获取联系人方式
        Contacts=ab.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/dl/dd/a[1]//text()')

        compan=ab.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/h4//text()')


        #获取主要信息模块
        lit=ab.xpath('//*[@id="site_content"]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]//text()')




        # 写入厂家及联系人姓名职位
        m.write(compan[0])
        m.write("\n")
        m.write(Contacts[0])
        m.write("\n")

        # 写入具体数据
        for i in  lit:
            m.write(i)
except:

# 关闭文件
    m.close()
