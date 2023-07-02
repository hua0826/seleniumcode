from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

driver.maximize_window()
time.sleep(2)
driver.set_window_size(800, 600)
time.sleep(2)
driver.set_window_position(200, 200)
time.sleep(2)

driver.find_element(By.ID, "kw").send_keys("南京天气")
driver.find_element(By.ID, "su").click()

print(driver.title)
print(driver.current_url)

time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
driver.maximize_window()
time.sleep(2)
# driver.find_element(By.LINK_TEXT, "hao123").click()
driver.find_element(By.XPATH,"//*[text()='hao123']").click()
time.sleep(2)
driver.close()

time.sleep(3)

driver.quit()
