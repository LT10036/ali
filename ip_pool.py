
import selenium
from     selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 设置浏览器
opt=Options()
opt.add_argument("disable-infobars")
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")


f = open("ips.txt","a",encoding="utf-8")



# 打开浏览器开始第一页
driver=webdriver.Chrome(chrome_options=opt)
driver.get("https://www.kuaidaili.com/free/")

# 大模块
ns=driver.find_elements_by_xpath('//*[@id="list"]/table/tbody/tr')

# 小模块
for i in ns:
    ips=i.find_element_by_xpath("./td[1]").text
    port=i.find_element_by_xpath("./td[2]").text
    f.write(ips)
    f.write(":")
    f.write(port)
    f.write("\n")



# 第二页往后
for url in range(2,10):
    m="https://www.kuaidaili.com/free/inha/"+str(url) +"/"

    driver.get(m)

    ns = driver.find_elements_by_xpath('//*[@id="list"]/table/tbody/tr')

    for i in ns:
        ips = i.find_element_by_xpath("./td[1]").text
        port = i.find_element_by_xpath("./td[2]").text
        f.write(ips)
        f.write(":")
        f.write(port)
        f.write("\n")

# 关闭文件
f.close()


