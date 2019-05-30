import selenium
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# 取消检测浏览器是否被控制
opt=Options()
opt.add_argument("disable-infobars")

f=open("hclb.txt","a")

# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)
driver.get("https://s.hc360.com/seller/search.html?kwd=%E6%B4%97%E8%A1%A3%E6%9C%BA&pnum=2&ee=2")
driver.maximize_window()

# 下滑滚动条
while True:
    time.sleep(5)
    i=0
    m=760
    while i<5:
        s='window.scrollTo(0,%d)'%m
        driver.execute_script(s)
        i=i+1
        m=1000+m
        time.sleep(3)

#  大标签
    n=driver.find_elements_by_xpath('/html/body/div[3]/div[7]/div[2]/div[2]/ul/li')

    # 循环小标签找出链接,写入文本
    for i in n:
        hre=i.find_element_by_xpath('./div/div/a').get_attribute("href")
        f.write(hre)
        f.write("\n")

    #
    #下一页点击
    try:
        nex = driver.find_element_by_xpath('//*[@id="clip"]/div/span[4]/a').get_attribute("href")
        driver.find_element_by_xpath('//*[@id="clip"]/div/span[4]/a').click()
        time.sleep(3)
    except :

        # 关闭文本，关闭浏览器
        f.close()
        driver.quit()








