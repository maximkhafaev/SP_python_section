from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class DemoShopLoginPage:

    """
    Класс для работы со страницей авторизации
    """

    __USERNAME_INPUT_FIELD = (By.ID, 'user-name')
    __PASSWORD_INPUT_FIELD = (By.ID, 'password')
    __LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):

        """
        Конструктор класса DemoShopLoginPage

        :param driver: WebDriver — объект драйвера Selenium
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открываем интернет-магазин")
    def open_demo_shop_login_page(self):

        """
        Открывает страницу авторизации
        """

        self.driver.get(
            'https://www.saucedemo.com/'
        )

    @allure.step("Авторизуемся под пользователем standard_user:secret_sauce")
    def authorize(self):

        """
        Авторизует в магазине под пользователем standard_user:secret_sauce
        """

        self.wait.until(EC.visibility_of_element_located(
            self.__USERNAME_INPUT_FIELD
        )).send_keys('standard_user')
        self.wait.until(EC.presence_of_element_located(
            self.__PASSWORD_INPUT_FIELD
        )).send_keys('secret_sauce')
        self.driver.find_element(*self.__LOGIN_BUTTON).click()
