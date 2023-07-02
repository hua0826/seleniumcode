from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

url = "https://testnet.app.zkex.com/"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)
driver.implicitly_wait(5)
# select = Select(driver.find_element(By.CLASS_NAME,"sc-iFwKgL eTHiiz"))
# time.sleep(2)
# select.select_by_index(3)     #根据索引，从0开始
# select.select_by_value()     #根据属性value值
# select.deselect_by_visible_text()  #根据文本值

driver.find_element(By.CLASS_NAME,"eTHiiz").click()
time.sleep(2)
el = driver.find_elements(By.CLASS_NAME,"gaWCVe")
print(len(el))
for e in el:
    if "BSC Testnet" in e.text:
        print(e.text)
        e.click()
        break


time.sleep(3)
driver.quit()
