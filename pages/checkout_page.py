from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.confirm_msg = (By.CLASS_NAME, "complete-header")

    def enter_details(self, fname, lname, zipcode):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zipcode)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def get_confirmation(self):
        return self.driver.find_element(*self.confirm_msg).text
