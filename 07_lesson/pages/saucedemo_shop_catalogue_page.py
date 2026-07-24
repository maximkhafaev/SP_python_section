from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoShopCataloguePage:

    SAUCE_LABS_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    SAUCE_LABS_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    SAUCE_LABS_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_BUTTON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_items_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(
            self.SAUCE_LABS_BACKPACK
        )).click()
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        self.wait.until(EC.visibility_of_element_located(
            self.SAUCE_LABS_BOLT_TSHIRT
        )).click()
        self.wait.until(EC.visibility_of_element_located(
            self.SAUCE_LABS_ONESIE
        )).click()

    def go_to_cart(self):
        self.driver.execute_script('window.scrollTo(0, 0)')
        self.wait.until(EC.visibility_of_element_located(
            self.CART_BUTTON
        )).click()
