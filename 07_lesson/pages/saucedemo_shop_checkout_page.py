from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoShopCheckoutPage:

    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_TEXT = (By.CSS_SELECTOR, 'div[data-test="total-label"]')

    def __init__(self, driver, first_name, last_name, postal_code):
        self.driver = driver
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
        self.wait = WebDriverWait(self.driver, 10)

    def fill_customer_information(self):
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME_FIELD
        )).send_keys(self.first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME_FIELD
        )).send_keys(self.last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.POSTAL_CODE_FIELD
        )).send_keys(self.postal_code)

    def press_continue(self):
        self.wait.until(EC.visibility_of_element_located(
            self.CONTINUE_BUTTON
        )).click()

    def read_total(self):
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        return self.driver.find_element(*self.TOTAL_TEXT).text
