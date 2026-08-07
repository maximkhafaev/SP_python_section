from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class DemoShopCheckoutPage:

    """
    Класс для работы со страницей оформления заказа
    """

    __FIRST_NAME_FIELD = (By.ID, 'first-name')
    __LAST_NAME_FIELD = (By.ID, 'last-name')
    __POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    __CONTINUE_BUTTON = (By.ID, 'continue')
    __TOTAL_TEXT = (By.CSS_SELECTOR, 'div[data-test="total-label"]')

    @allure.step("Фиксируем контактные данные пользователя: "
                 "имя — {first_name}, фамилия — {last_name}"
                 ", почтовый индекс — {postal_code}")
    def __init__(self, driver, first_name: str, last_name: str,
                 postal_code: str):

        """
        Конструктор класса DemoShopCheckoutPage

        :param driver: WebDriver — объект драйвера Selenium
        :param first_name: str — имя клиента
        :param last_name: str — фамилия клиента
        :param postal_code: str — почтовый индекс
        """

        self.driver = driver
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Заполняем данные клиента: имя, фамилию и почтовый индекс")
    def fill_customer_information(self) -> None:

        """
        Заполняет контактную информацию клиента
        """

        self.wait.until(EC.visibility_of_element_located(
            self.__FIRST_NAME_FIELD
        )).send_keys(self.first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.__LAST_NAME_FIELD
        )).send_keys(self.last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.__POSTAL_CODE_FIELD
        )).send_keys(self.postal_code)

    @allure.step("Подтверждаем данные")
    def press_continue(self):

        """
        Нажимает кнопку Дальше
        """

        self.wait.until(EC.visibility_of_element_located(
            self.__CONTINUE_BUTTON
        )).click()

    @allure.step("Читаем итоговую сумму")
    def read_total(self) -> str:

        """
        Читает итоговую сумму

        :return str: Текст итоговой суммы заказа
        """

        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)')
        return self.driver.find_element(*self.__TOTAL_TEXT).text
