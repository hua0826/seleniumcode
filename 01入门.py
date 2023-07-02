from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

url = "http://baidu.com"

driver.get(url)

time.sleep(5)

driver.quit()
