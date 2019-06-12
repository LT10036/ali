import  selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 打开一个文本记录店铺地址
f=open("pig66.txt","a")

# 取消检测浏览器被控制提示
opt=Options()
opt.add_argument("disable-infobars")

# 打开浏览器
driver=webdriver.Chrome(chrome_options=opt)
driver.maximize_window()

driver.get('http://www.pig66.com/120/12.html')

for scor in range(4):

    time.sleep(5)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

    m = driver.find_elements_by_xpath('//*[@id="title"]/a')
    for i in m:
        hre = i.get_attribute('href')
        f.write(hre)
        f.write('\n')


    driver.find_element_by_xpath('/html/body/div[9]/div[4]/div[1]/div/div[2]/div/a[13]').click()

f.close()