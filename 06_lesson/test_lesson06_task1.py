from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    # 2. Найдите и нажмите на кнопку "Start"
    start_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#start button")
    ))
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    loaded_text = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#finish  h4")
    ))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/task1_scr.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert loaded_text.text == 'Hello World!'

    driver.quit()
