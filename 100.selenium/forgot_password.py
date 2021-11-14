from selenium  import webdriver
from selenium.webdriver.chrome.service import Service

import time
from selenium .webdriver.common.keys import Keys

ser = Service(r"browsers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
print("sample test case started")

driver.maximize_window()
#navigate to the url
driver.get("http://www.google.com/")
time.sleep(3)

driver.close()
print("sample test case successfully completed")