from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
print("simple test case started")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(by=By.NAME,value='q').send_keys("Javatpoint")
time.sleep(3)
driver.find_element(by=By.NAME,value='btnK').send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
print("sample test case completed")
