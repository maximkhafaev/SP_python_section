import time
from pages.calculator_page import CalculatorPage


def test_calc(chrome_driver):
    calculator = CalculatorPage(chrome_driver, 45)
    calculator.open_calculator_page()
    calculator.enter_delay()
    calculator.perform_calculations()
    start = time.time()
    calculator.wait_for_the_calculation_result()
    end = time.time()

    assert round(end - start) == 45
