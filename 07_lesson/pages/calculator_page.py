from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY_INPUT_BOX = (By.ID, 'delay')
    NUMBER_7_BUTTON = (By.XPATH, '//span[text()="7"]')
    NUMBER_8_BUTTON = (By.XPATH, '//span[text()="8"]')
    PLUS_BUTTON = (By.XPATH, '//span[text()="+"]')
    RESULT_BUTTON = (By.XPATH, '//span[text()="="]')
    RESULT_FIELD = (By.CSS_SELECTOR, 'div.screen')

    def __init__(self, driver, delay):
        self.driver = driver
        self.delay = delay
        self.wait = WebDriverWait(self.driver, self.delay)

    def open_calculator_page(self):
        self.driver.get(
         'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def enter_delay(self):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT_BOX)
        )
        delay_input.clear()
        delay_input.send_keys(self.delay)

    def perform_calculations(self):
        self.driver.find_element(*self.NUMBER_7_BUTTON).click()
        self.driver.find_element(*self.PLUS_BUTTON).click()
        self.driver.find_element(*self.NUMBER_8_BUTTON).click()
        res_button = self.driver.find_element(*self.RESULT_BUTTON)
        self.driver.execute_script("arguments[0].click();", res_button)

    def wait_for_the_calculation_result(self):
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT_FIELD, '15')
        )
