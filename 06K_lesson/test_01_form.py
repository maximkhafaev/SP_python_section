# Шаги
# 1. Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в Edge или Safari.
# 2. Заполните форму значениями:
# First name Иван
# Last name Петров
# Address Ленина, 55-3
# Email test@skypro.com
# Phone number +7985899998787
# Zip code *оставить пустым
# City Москва
# Country Россия
# Job position QA
# Company SkyPro
# 3. Нажмите кнопку Submit.
# 4. Проверьте, что поле Zip code подсвечено красным.
# 5. Проверьте, что остальные поля подсвечены зеленым


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Safari()
    wait = WebDriverWait(driver, 2)
    driver.maximize_window()

    # 1. Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    # в Edge или Safari.
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # 2. Заполните форму значениями
    driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]'
        ).send_keys('Иван')
    driver.find_element(
        By.CSS_SELECTOR, '[name="last-name"]'
        ).send_keys('Петров')
    driver.find_element(
        By.CSS_SELECTOR, '[name="address"]'
        ).send_keys('Ленина, 55-3')
    driver.find_element(
        By.CSS_SELECTOR, '[name="city"]'
        ).send_keys('Москва')
    driver.find_element(
        By.CSS_SELECTOR, '[name="country"]'
        ).send_keys('Россия')
    driver.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]'
        ).send_keys('test@skypro.com')
    driver.find_element(
        By.CSS_SELECTOR, '[name="phone"]'
        ).send_keys('+7985899998787')
    driver.find_element(
        By.CSS_SELECTOR, '[name="job-position"]'
        ).send_keys('QA')
    driver.find_element(
        By.CSS_SELECTOR, '[name="company"]'
        ).send_keys('SkyPro')

    # 3. Нажмите кнопку Submit.
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    driver.execute_script("arguments[0].click();", submit_btn)

    # 4. Проверьте, что поле Zip code подсвечено красным
    zip_code = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")
    ))
    assert zip_code.value_of_css_property(
        'background-color') == 'rgb(248, 215, 218)'

    # 5. Проверьте, что остальные поля подсвечены зеленым
    elements = driver.find_elements(By.CLASS_NAME, 'alert-success')
    for element in elements:
        assert element.value_of_css_property(
            'background-color') == 'rgb(209, 231, 221)'

    driver.quit()
