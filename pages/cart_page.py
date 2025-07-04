from selenium.webdriver.common.by import By
class CartPage:
     def __init__(self, driver):
         self.driver = driver
         self.remove_btn=(By.ID, "remove-sauce-labs-backpack")
         self.checkout_btn=(By.ID, "checkout")

     def remove_item(self):
        self.driver.find_element(*self.remove_btn).click()

     def proceed_to_checkout(self):
       self.driver.find_element(*self.checkout_btn).click()