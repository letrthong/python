# selenium = "4.0.0" Window  10 -64 bit
# https://selenium-python.readthedocs.io/navigating.html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

ser = Service(r"browsers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()
driver.get("https://updater-neon-bot-dev-01.ngrok.io/")
time.sleep(1)
select = Select(driver.find_element(By.ID, "id_header_language"))
select.select_by_index(2)

try:
    time.sleep(3)
except:
    print("An exception occurred")

driver.close()
driver.quit()

