from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "https://mail.qq.com/"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)

# print(driver.find_element(By.CLASS_NAME, "login_pictures_title").text) #获取原始页面原始属性


driver.switch_to.frame(1)   #切换frame界面

driver.switch_to.frame('ptlogin_iframe')  #切换第二层frame

driver.find_element(By.ID,"switcher_plogin").click()

driver.find_element(By.ID,"u").send_keys("100001")

time.sleep(2)

driver.switch_to.default_content()   #返回原始的页面

print(driver.find_element(By.CLASS_NAME, "login_pictures_title").text) #获取原始页面原始属性


time.sleep(2)
driver.quit()


