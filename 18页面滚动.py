from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "https://www.douyu.com/directory/all"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

driver.maximize_window()
time.sleep(2)
js_str = "window.scrollTo(0,10000)"
driver.execute_script(js_str)




time.sleep(3)
driver.quit()
