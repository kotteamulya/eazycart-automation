import time
from selenium.common import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import loginPage
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.order(4)  # First test
def test_logout_with_excel(driver):
    ...

def test_valid_logout_with_excel(driver):
    driver.get("https://www.saucedemo.com/")  # ✅ Add this line

    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass

    # rest of the code...


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))

    login_page = loginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    time.sleep(1)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    assert driver.find_element(By.ID, "login-button").is_displayed()
    time.sleep(3)



