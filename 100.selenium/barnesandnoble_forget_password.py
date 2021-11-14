# selenium = "4.0.0" Window  10 -64 bit
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

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
# Clicking on "Sign in" button
time.sleep(1)
driver.find_element(By.XPATH,
                    "//a[@class=' rhf-sign-in rhf-myaccount-menu-item btn btn--medium'][contains(@href, '#')]").click()
time.sleep(4)
save_screenshot(driver)

# Process Dialog


# https://www.selenium.dev/documentation/webdriver/browser_manipulation/#frames-and-iframes
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
for iframe in iframes:
    title = iframe.get_attribute("title")
    if title is not None:
        if title == "Sign in or Create an Account":
            driver.switch_to.frame(iframe)
            driver.find_element(By.ID, 'email').send_keys("letrthong@gmail.com")
            time.sleep(4)



time.sleep(4)
driver.switch_to.default_content()
driver.close()
driver.quit()
