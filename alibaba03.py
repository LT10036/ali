import  selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 打开一个文本记录店铺地址
f=open("123.txt","a")

# 取消检测浏览器被控制提示
opt=Options()
opt.add_argument("disable-infobars")

# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)
driver.maximize_window()

# 打开阿里巴巴查询页
driver.get("https://p4psearch.1688.com/p4p114/p4psearch/offer2.htm?keywords=%E8%8A%B1%E7%9B%86&cosite=baidujj&location=landing_t4&trackid=88568819612896757133395&keywordid=65055714817&format=normal&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA")


# 下滑列表取得单页所有商品模块
while True:
    time.sleep(5)
    i=0
    m=800

    while i<5:

        js='window.scrollTo(0,%d)'%m
        driver.execute_script(js)
        i=i+1
        m=1260+m
        time.sleep(3)


# 获取大模块，并找出子模块的地址链

    maxh=driver.find_elements_by_xpath('//*[@id="offerList"]/div/div/div[1]/div')

    # 写入
    for i in maxh:

        sl=i.find_element_by_xpath("./a").get_attribute("href")
        f.write(sl)
        f.write("\n")
    # 判断是否点击下一页
    fir=driver.find_element_by_xpath('//*[@id="offerList"]/div/div/div[2]/div/div/span/em').text
    ed=driver.find_element_by_xpath('//*[@id="offerList"]/div/div/div[2]/div/div/span').text

    # 获取对比值
    fir2=int(fir)
    en2=ed[2]+ed[3]
    ed3=int(en2)

    if fir2!=ed3:
        driver.find_element_by_xpath('//*[@id="offerList"]/div/div/div[2]/div/div/button[2]').click()

    else:
        break







