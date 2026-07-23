from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoShopCartPage:

    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_checkout(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        self.wait.until(EC.visibility_of_element_located(
            self.CHECKOUT_BUTTON
        )).click()
