from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("python教程")
driver.find_element(By.XPATH,"//*[@id='su']").click()

time.sleep(3)

driver.quit()
