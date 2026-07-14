# Шаги
# 1. Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# в Google Chrome
# 2. В поле ввода по локатору #delay введите значение 45
# 3. Нажмите на кнопки: 7, +, 8, =
# 4. Проверьте, что в окне отобразится результат 15 через 45 секунд


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    driver.maximize_window()

    # 1. Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    # в Google Chrome
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    footer = driver.find_element(By.CLASS_NAME, "footer")
    ActionChains(driver)\
        .scroll_to_element(footer)\
        .perform()

    # 2. В поле ввода по локатору #delay введите значение 45
    lenght = driver.find_element(By.ID, 'delay')
    lenght.clear()
    lenght.send_keys('45')

    # 3. Нажмите на кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    start = time.time()

    # 4. Проверьте, что в окне отобразится результат 15 через 45 секунд
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'div.screen'), '15'
    ))
    end = time.time()
    length = round(end - start)
    assert length == 45

    driver.quit()
