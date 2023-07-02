from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

el = driver.find_element(By.ID,"kw")
el.send_keys("python")  #输入
time.sleep(2)
el.send_keys(Keys.CONTROL,"a")  #全选
time.sleep(2)
el.send_keys(Keys.BACKSPACE)  #删除
time.sleep(2)

el.send_keys("你来打我呀")  #输入
time.sleep(2)
el.send_keys(Keys.CONTROL,"a")  #全选
time.sleep(2)
el.send_keys(Keys.CONTROL,"c")  #复制
time.sleep(2)
el.send_keys(Keys.BACKSPACE)  #删除
time.sleep(2)
el.send_keys(Keys.CONTROL,"v")  #粘贴

time.sleep(3)
driver.quit()
