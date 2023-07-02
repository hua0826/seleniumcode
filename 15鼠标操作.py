from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

url = "http://baidu.com"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

action = ActionChains(driver)
# action.context_click(driver.find_element(By.ID,"su"))
action.move_to_element(driver.find_element(By.CLASS_NAME,"soutu-btn"))
# action.drag_and_drop(driver.find_element(By.ID,"div1"),driver.find_element(By.ID,"div2"))
action.perform()

time.sleep(3)
driver.quit()
