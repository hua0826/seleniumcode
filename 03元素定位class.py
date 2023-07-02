from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("python教程")
driver.find_element(By.CLASS_NAME, "s_btn").click()

time.sleep(2)

driver.quit()
