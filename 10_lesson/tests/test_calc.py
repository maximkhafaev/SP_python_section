from pages.calculator_page import CalculatorPage
import allure


@allure.parent_suite("LESSON_10")
@allure.suite("CALC")
@allure.title("Тестирование калькулятора c задержкой")
@allure.description("Тестирует страницу калькулятора, который "
                    "выводит результат с задержкой, на "
                    "операции 7 + 8")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(chrome_driver):
    calculator = CalculatorPage(chrome_driver, 45)
    calculator.open_calculator_page()
    calculator.enter_delay()
    calculator.perform_calculations()
    result = calculator.wait_for_the_calculation_result()

    with allure.step("Проверка результата вычислений"):
        assert result == '15'
