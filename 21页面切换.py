from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)
driver.maximize_window()

driver.find_element(By.ID,"kw").send_keys("美女")
driver.find_element(By.ID,"su").click()

time.sleep(2)
driver.find_element(By.ID,"1").click()

time.sleep(2)






time.sleep(2)
driver.quit()


