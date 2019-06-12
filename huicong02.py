import selenium
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import random


# selenium添加代理

# ipss=[]
#
# # 打开代理池文本
# f=open("ips.txt","r",encoding="utf-8")
# while True:
#     ips=f.readline()
#     if not ips :
#         f.close()
#         break
#     else:
#         ipss.append(ips)
#
# # 随机数选择 代理ip
# sj = random.randint(0,len(ipss))
# sjip = ipss[sj]


# 取消检测浏览器是否被控制,添加随机 ip

opt=Options()

opt.add_argument("disable-infobars")
prefs = {"profile.managed_default_content_settings.images": 2}
opt.add_argument('--proxy-server=http://60.10.2.70:3128')
opt.add_experimental_option("prefs", prefs)
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")


# 打开目标源文本
hcc=open("hc_list.txt","r")


# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)

while True:

    # 没写停止判断，直接读取并开始操作
    her=hcc.readline()
    if not her:
        break
    else:

        try:
            # 新建存储文本，结束后找----慧聪网数据清洗.py-------
            whc = open("hc.txt", "a",encoding="utf-8")
            driver.get(her)

            # 点击获取联系方式
            driver.find_element_by_xpath('//*[@id="checkContactBtn"]').click()
            time.sleep(2)

            # 测试获取数据
            try:
                tel = driver.find_element_by_class_name('cardBox').text
            except:
                tel=driver.find_element_by_class_name('word-box').text
            print(her)
            print(tel)
            whc.write(tel)
            whc.write("\n")
            whc.close()
        except:
            continue


