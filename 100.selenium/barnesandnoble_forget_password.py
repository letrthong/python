# selenium = "4.0.0" Window  10 -64 bit
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

ser = Service(r"browsers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()
driver.get("https://www.barnesandnoble.com/h/books/browse")

# Show "Sign in" button  <a class= "nav-link   rhf-nav-link" id="navbarDropdown  href="#" >
driver.find_element(By.XPATH,
                    "//a[@class='nav-link   rhf-nav-link' and @id='navbarDropdown'][contains(@href, '#')]").click()
# Clicking on" Sign in" button
time.sleep(1)
driver.find_element(By.XPATH,
                    "//a[@class=' rhf-sign-in rhf-myaccount-menu-item btn btn--medium'][contains(@href, '#')]").click()
time.sleep(6)
# Go to forgot your password in form
driver.find_element(By.XPATH, "//a[@id='loginForgotPassword'][contains(@href, '#')]").click()

time.sleep(6)

driver.close()
driver.quit()
