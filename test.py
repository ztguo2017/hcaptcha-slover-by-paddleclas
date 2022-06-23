import time

import undetected_chromedriver as uc
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = uc.Chrome(
                  # 10daadc51e909_chromedriver.exe',
                  #  browser_executable_path=r"C:\Users\ztguo\Desktop\gov_chrome\gov_chrome.exe",
                   use_subprocess=True,
    version_main=103,
headless=False)
# 代理服务器
driver.get("http://httpbin.org/ip")
print(driver.current_url)
print(driver.page_source)
# time.sleep(10000)
# time.sleep(3)
driver.close()
import os
s = os.path.abspath(os.path.expanduser('~/.local/share/undetected_chromedriver'))
print(s)