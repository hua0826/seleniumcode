from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

print(driver.find_element(By.ID, "kw").size)
print(driver.find_element(By.ID, "kw").text)
print(driver.find_element(By.ID, "su").is_displayed())
print(driver.find_element(By.ID, "su").is_enabled())
print(driver.find_element(By.ID, "kw").get_attribute("class"))

time.sleep(3)

driver.quit()
