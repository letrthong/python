# selenium = "4.0.0" Window  10 -64 bit
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service(r"browsers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element(By.NAME, 'q').send_keys("selenium in python")
time.sleep(3)

driver.find_element(By.NAME, 'btnK').send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
driver.quit()
