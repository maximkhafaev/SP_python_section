from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class DemoShopCataloguePage:

    """
    Класс для работы со страницей каталога интернет-магазина
    """

    __SAUCE_LABS_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    __SAUCE_LABS_BOLT_TSHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    __SAUCE_LABS_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    __CART_BUTTON = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def __init__(self, driver):

        """
        Конструктор класса DemoShopCataloguePage

        :param driver: WebDriver — объект драйвера Selenium
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Добавляем товары SAUCE_LABS_BACKPACK, "
                 "SAUCE_LABS_BOLT_TSHIRT и SAUCE_LABS_ONESIE в корзину")
    def add_items_to_cart(self):

        """
        Добавляет товары SAUCE_LABS_BACKPACK, SAUCE_LABS_BOLT_TSHIRT
        и SAUCE_LABS_ONESIE в корзину
        """

        self.wait.until(EC.visibility_of_element_located(
            self.__SAUCE_LABS_BACKPACK
        )).click()
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        self.wait.until(EC.visibility_of_element_located(
            self.__SAUCE_LABS_BOLT_TSHIRT
        )).click()
        self.wait.until(EC.visibility_of_element_located(
            self.__SAUCE_LABS_ONESIE
        )).click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):

        """
        Переходит в корзину из каталога
        """

        self.driver.execute_script('window.scrollTo(0, 0)')
        self.wait.until(EC.visibility_of_element_located(
            self.__CART_BUTTON
        )).click()
