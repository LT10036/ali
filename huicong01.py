
# -------------------------------------------------------------------------------------

#  总 注 释 千 万 注 意 ：
# 网 站 商 品 展 示 页  面 根 据 产 品 种 类 不 同，  需 要 修改 x p a th
#  可 能 会 出 现 xp t h 匹 配 定  位不 上 的  问题


#-------------------------------------------------------------------------------------

import selenium
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# 创建建总商品链接网址

Website = "https://s.hc360.com/seller/search.html?ap=B&z=%E4%B8%AD%E5%9B%BD:%E6%B2%B3%E5%8C%97%E7%9C%81:%E7%9F%B3%E5%AE%B6%E5%BA%84%E5%B8%82&w=%E5%AE%B6%E5%85%B7&nselect=1&combine=&j=0&v=1&pnum=4&ee=4"
# 取消检测浏览器是否被控制  # 不加载图片，设置的参数很固定
prefs = {"profile.managed_default_content_settings.images": 2}
opt=Options()
opt.add_argument("disable-infobars")
opt.add_experimental_option("prefs", prefs)

# 新建一个存储商家链接的文本，供 02 直接读取调用
f=open("hc_list.txt","a")

# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)
driver.get(Website)
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
    n=driver.find_elements_by_class_name('grid-list')

    # 循环小标签找出链接,写入文本
    for i in n:
        hre=i.find_element_by_xpath('./div/div/a').get_attribute("href")
        f.write(hre)
        f.write("\n")


    #下一页点击
    try:
        nex = driver.find_element_by_link_text('下一页').get_attribute("href")
        driver.find_element_by_link_text('下一页').click()
        time.sleep(3)
    except :

        # 关闭文本，关闭浏览器
        f.close()
        driver.quit()








