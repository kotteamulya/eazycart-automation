import time
from pages.login_page import loginPage
from selenium.webdriver.common.by import By



def test_logout(driver):
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



