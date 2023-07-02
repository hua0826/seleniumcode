from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

# driver.find_element(By.ID, "kw").send_keys("美女")
driver.find_element(By.ID, "kw").send_keys("python教程")
driver.find_element(By.ID, "su").click()

time.sleep(3)

# driver.find_element(By.CLASS_NAME, "c-container").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "项目实战—慕课网").click()
driver.find_element(By.XPATH, "//*[text()='项目实战—慕课网']").click()
time.sleep(5)


driver.quit()
