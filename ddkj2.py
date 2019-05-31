

# https://zhongbao.istarshine.com/task/mine


import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from lxml import etree


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://ddkjj.dandong.gov.cn/")

#
# 新建文档存储地址
f=open("321.txt","a")
# 创建列表

lsx=['//*[@id="zwgk_floor"]/div/div[8]/div[1]/span/a','//*[@id="zwgk_floor"]/div/div[7]/div[1]/span/a','//*[@id="zwgk_floor"]/div/div[6]/div[1]/span/a',
     '//*[@id="zwgk_floor"]/div/div[3]/div[1]/span/a','//*[@id="zwgk_floor"]/div/div[2]/div[1]/span/a']

# 第一次提取数据
for i in lsx:

    # 点击更多
    driver.find_element_by_xpath(i).click()
    time.sleep(2)

    # 第一页提取
    lis = driver.find_elements_by_xpath('//*[@id="floor"]/div/div[2]/div[2]/ul/li')

    # 小链接提取
    for n in lis:
        hre=n.find_element_by_xpath("./a").get_attribute("href")
        f.write(hre)
        f.write("\n")
#开始try下一页
    try:
        # 循环点击下一页
        while True:

            # 点击下一页
            driver.find_element_by_link_text("下一页").click()
            time.sleep(3)

            # 大模块提取
            lis = driver.find_elements_by_xpath('//*[@id="floor"]/div/div[2]/div[2]/ul/li')

            # 小标签链接提取
            for i in lis:
                hre = i.find_element_by_xpath("./a").get_attribute("href")

                # 写入
                f.write(hre)
                f.write("\n")
    # 没有找到下一页，则报错进入点击回到主页
    except:
        driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/a[1]').click()
        time.sleep(2)
driver.quit()
f.close()


# 开始读取
m=open("321.txt",encoding='utf-8')
while True:
    mn=m.readline()

    # 开始请求连接
    sour=requests.get(mn)
    sour2=sour.text

    # 转换源码
    xl=etree.HTML(sour2)

    # 开始提取
    pass








