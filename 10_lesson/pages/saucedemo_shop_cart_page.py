from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class DemoShopCartPage:

    """
    Класс для работы со страницей корзины интернет-магазина
    """

    __CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver) -> None:

        """
        Конструктор класса DemoShopCartPage

        :param driver: WebDriver — объект драйвера Selenium
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Переходим из корзины на страницу оформления заказа")
    def go_to_checkout(self) -> None:

        """
        Переходит из корзины на страницу оформления заказа
        """

        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        self.wait.until(EC.visibility_of_element_located(
            self.__CHECKOUT_BUTTON
        )).click()
