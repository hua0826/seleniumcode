from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

driver.find_element(By.NAME, "wd").send_keys("python教程")
driver.find_element(By.ID, "su").click()

time.sleep(5)

driver.quit()
