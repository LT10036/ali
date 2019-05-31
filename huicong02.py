import selenium
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# 取消检测浏览器是否被控制

opt=Options()
opt.add_argument("disable-infobars")
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")

hcc=open("hclb.txt","r")


# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)

while True:

    her=hcc.readline()

    whc = open("hc.txt", "a",encoding="utf-8")
    driver.get(her)

    # 点击获取联系方式
    driver.find_element_by_xpath('//*[@id="checkContactBtn"]').click()
    time.sleep(2)

    # 测试获取数据
    tel = driver.find_element_by_xpath('//*[@id="dialogCorMessage"]').text
    print(tel)
    whc.write(tel)
    whc.write("\n")
    whc.write("...................................")
    whc.write("\n")
    whc.close()

