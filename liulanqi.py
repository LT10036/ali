from selenium import webdriver
import time
from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException




# 重写浏览器打开方法，使用之前打开的浏览器进行操作，可以注释掉
class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False


#      打开浏览器
opt=webdriver.ChromeOptions()
opt.add_argument("disable-infobars")
driver=webdriver.Chrome(chrome_options=opt)
newurl = driver.command_executor._url
seesiond = driver.session_id

driver.get("https://baidu.com")

time.sleep(5)




# 第二次打开
driver2=ReuseChrome(command_executor=newurl,session_id=seesiond)
driver2.get("https://www.sina.com.cn/")
time.sleep(3)

driver3=ReuseChrome(command_executor=newurl,session_id=seesiond)
driver3.get("https://www.qq.com/")
