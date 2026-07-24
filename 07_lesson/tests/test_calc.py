from pages.calculator_page import CalculatorPage


def test_calc(chrome_driver):
    calculator = CalculatorPage(chrome_driver, 5)
    calculator.open_calculator_page()
    calculator.enter_delay()
    calculator.perform_calculations()
    result = calculator.wait_for_the_calculation_result()

    assert result == '15'
