from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://testnet.app.zkex.com/"

path = Service("chromedriver.exe")

driver = webdriver.Chrome(service=path)

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH,"//*[text()='Connect Wallet']").click()

# wait = WebDriverWait(driver,10)
# wait.until(EC.alert_is_present()) #等待直到弹框出现
alter = driver.switch_to.alert  #切换至弹框
print(alter.text)
alter.accept()
alter.dismiss()
alter.send_keys()



time.sleep(3)
driver.quit()
