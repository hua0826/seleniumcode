from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

driver.find_element(By.ID, "kw").send_keys("python教程")
driver.find_element(By.ID, "su").click()

WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wbrjf67")))

driver.find_element(By.CLASS_NAME, "wbrjf67").click()

time.sleep(5)

driver.quit()
