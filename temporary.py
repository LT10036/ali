import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


opt = Options()
opt.add_argument("disable-infobars")

driver = webdriver.Chrome(chrome_options=opt)


driver.get("https://s.hc360.com/?w=%E5%9B%BE%E6%A1%88%E7%81%AF&mc=seller")



m=driver.find_elements_by_class_name("grid-list")


for i in m:
    l = i.find_element_by_xpath("./div/div[1]/a").get_attribute("href")

    print(l)
time.sleep(10)
nex = driver.find_element_by_link_text('下一页').get_attribute("href")
driver.find_element_by_link_text('下一页').click()