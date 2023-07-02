from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

# driver.find_element(By.LINK_TEXT, "hao123").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"hao1").click()


time.sleep(2)

driver.quit()
