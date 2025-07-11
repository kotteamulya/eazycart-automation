from selenium.webdriver.common.by import By
class loginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


