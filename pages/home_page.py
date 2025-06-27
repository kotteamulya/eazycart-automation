from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn=(By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon=(By.XPATH, "//a[@class='shopping_cart_link']")
    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()