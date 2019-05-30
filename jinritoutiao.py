

import selenium
import time
from selenium import webdriver




# 打开主页

driver=webdriver.Chrome()

driver.get("https://mp.qutoutiao.net")

time.sleep(5)
#
# # 定位实现登录
#
#
try:
    login=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[11]/div/div[2]/form/div[1]/div/input').click()
    time.sleep(2)

    # # 选择账号密码登录
    # zm=driver.find_element_by_xpath('//*[@id="login-type-account"]/img').click()
    #
    # time.sleep(3)
    # # 输入账号密码
    #
    zh=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[11]/div/div[2]/form/div[1]/div/input').click()
    zh2=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[11]/div/div[2]/form/div[1]/div/input').send_keys("13266915913")
    time.sleep(2)


    sc=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[11]/div/div[2]/form/div[2]/div/input').click()
    time.sleep(3)

    sc2=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[11]/div/div[2]/form/div[2]/div/input').send_keys("zx850625")

    time.sleep(2)


    # 登录

    loging=driver.find_element_by_xpath('//*[@id="submit-login"]/span').click()




except:

    driver.quit()






