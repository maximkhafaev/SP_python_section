from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:

    """
    Класс для взаимодействия со страницей калькулятора через Selenium
    """

    __DELAY_INPUT_BOX = (By.ID, 'delay')
    __NUMBER_7_BUTTON = (By.XPATH, '//span[text()="7"]')
    __NUMBER_8_BUTTON = (By.XPATH, '//span[text()="8"]')
    __PLUS_BUTTON = (By.XPATH, '//span[text()="+"]')
    __RESULT_BUTTON = (By.XPATH, '//span[text()="="]')
    __RESULT_FIELD = (By.CSS_SELECTOR, 'div.screen')

    @allure.step("Задание задержки в {delay} секунд")
    def __init__(self, driver, delay: int):

        """
        Конструктор класса CalculatorPage

        :param driver: WebDriver — объект драйвера Selenium
        :param delay: int — продолжительность задержки в секундах
        """

        self.driver = driver
        self.delay = delay
        self.wait = WebDriverWait(self.driver, self.delay)

    @allure.step("Открытие страницы калькулятора")
    def open_calculator_page(self) -> None:

        """
        Открывает страницу калькулятора
        """

        self.driver.get(
         'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step("Установка задержки на странице калькулятора")
    def enter_delay(self) -> None:

        """
        Устанавливает задержку отображения результата вычислений
        """

        delay_input = self.wait.until(
            EC.presence_of_element_located(self.__DELAY_INPUT_BOX)
        )
        delay_input.clear()
        delay_input.send_keys(self.delay)

    @allure.step("Нажатие кнопок калькулятора '7', "
                 "'+', '8' и '='")
    def perform_calculations(self) -> None:

        """
        Нажимает кнопки калькулятора: 7, +, 8, =
        """

        self.driver.find_element(*self.__NUMBER_7_BUTTON).click()
        self.driver.find_element(*self.__PLUS_BUTTON).click()
        self.driver.find_element(*self.__NUMBER_8_BUTTON).click()
        res_button = self.driver.find_element(*self.__RESULT_BUTTON)
        self.driver.execute_script("arguments[0].click();", res_button)

    @allure.step(
            "Ожидание появления результата \"15\" после заданной задержки")
    def wait_for_the_calculation_result(self) -> str:

        """
        Ожидает появления результата вычислений после заданной задержки

        Возвращает текст результата с экрана калькулятора после его появления

        :return str: Текст результата на экране калькулятора
        """

        self.wait.until(EC.text_to_be_present_in_element(
            self.__RESULT_FIELD, '15')
        )
        self.res = self.driver.find_element(*self.__RESULT_FIELD).text
        return self.res
