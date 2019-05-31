# import selenium
# from  selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# # 取消检测浏览器是否被控制
# opt=Options()
# opt.add_argument("disable-infobars")
#
# f=open("hclb.txt","a")
#
# # 打开浏览器
# driver=webdriver.Chrome(chrome_options=opt)
# driver.get("https://s.hc360.com/seller/search.html?kwd=%E6%B4%97%E8%A1%A3%E6%9C%BA&pnum=96&ee=96")
#
#
# # 自己加载数据，无需滚动，等待3秒
# time.sleep(3)
# #
#
#
# time.sleep(5)
# i=0
# m=750
#
# while i<5:
#
#     s='window.scrollTo(0,%d)'%m
#     driver.execute_script(s)
#     i=i+1
#     m=1000+m
#     time.sleep(3)
# n = driver.find_elements_by_xpath('/html/body/div[3]/div[6]/div[2]/div[2]/ul/li')
#
#     # 循环小标签找出链接,写入文本
#
# for i in n:
#     hre = i.find_element_by_xpath('./div/div[1]/a').get_attribute("href")
#     print(hre)
#
#     f.write(hre)
#     f.write("\n")
# f.close()

ipss=[]

f=open("ips.txt","r",encoding="utf-8")
while True:
    ips=f.readline()
    if not ips :
        f.close()
        break
    else:
        ipss.append(ips)
print(ipss)







