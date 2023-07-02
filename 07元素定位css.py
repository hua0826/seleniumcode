from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

# driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("python教程")
# driver.find_element(By.CSS_SELECTOR,".s_ipt").send_keys("python教程")
driver.find_element(By.CSS_SELECTOR,"[name=wd]").send_keys("python教程")
driver.find_element(By.CSS_SELECTOR,"[value=百度一下]").click()

time.sleep(3)

driver.quit()
