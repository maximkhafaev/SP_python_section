from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoShopLoginPage:

    USERNAME_INPUT_FIELD = (By.ID, 'user-name')
    PASSWORD_INPUT_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_demo_shop_login_page(self):
        self.driver.get(
            'https://www.saucedemo.com/'
        )

    def authorize(self):
        self.wait.until(EC.visibility_of_element_located(
            self.USERNAME_INPUT_FIELD
        )).send_keys('standard_user')
        self.wait.until(EC.presence_of_element_located(
            self.PASSWORD_INPUT_FIELD
        )).send_keys('secret_sauce')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
