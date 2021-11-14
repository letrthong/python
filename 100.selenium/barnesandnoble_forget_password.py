# selenium = "4.0.0" Window  10 -64 bit
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


def save_screenshot(driver):
    driver.save_screenshot(".\screenshot\screenshot.png")


ser = Service(r"browsers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()
driver.get("https://www.barnesandnoble.com/h/books/browse")

main_page = driver.current_window_handle

# Show "Sign in" button  <a class= "nav-link   rhf-nav-link" id="navbarDropdown  href="#" >
driver.find_element(By.XPATH,
                    "//a[@class='nav-link   rhf-nav-link' and @id='navbarDropdown'][contains(@href, '#')]").click()
# Clicking on" Sign in" button
time.sleep(1)
driver.find_element(By.XPATH,
                    "//a[@class=' rhf-sign-in rhf-myaccount-menu-item btn btn--medium'][contains(@href, '#')]").click()
time.sleep(4)
save_screenshot(driver)

# Process Dialog
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id ='loginForgotPassword']")))
driver.find_element(By.ID, "loginForgotPassword").send_keys("xxxx@gmail.com")

driver.close()
driver.quit()
