# Шаги
# 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox
# 2. Авторизуйтесь как пользователь standard_user
# 3. Добавьте в корзину товары: Sauce Labs Backpack,
# Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
# 4. Перейдите в корзину
# 5. Нажмите Checkout
# 6. Заполните форму своими данными:
# имя, фамилия, почтовый индекс
# 7. Нажмите кнопку Continue
# 8. Прочитайте со страницы итоговую стоимость (Total)
# 9. Закройте браузер
# 10. Проверьте, что итоговая сумма равна $58.29


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 5)
    driver.maximize_window()

    # 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox
    driver.get('https://www.saucedemo.com/')

    # 2. Авторизуйтесь как пользователь standard_user
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'user-name')
    )).send_keys('standard_user')
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'password')
    )).send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # 3. Добавьте в корзину товары: Sauce Labs Backpack,
    # Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-backpack')
    )).click()
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    )).click()
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'add-to-cart-sauce-labs-onesie')
    )).click()

    # 4. Перейдите в корзину
    driver.execute_script('window.scrollTo(0, 0)')
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    )).click()

    # 5. Нажмите Checkout
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'checkout')
    )).click()

    # 6. Заполните форму своими данными
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'first-name')
    )).send_keys('Max')
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'last-name')
    )).send_keys('Khafaev')
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'postal-code')
    )).send_keys('630090')

    # 7. Нажмите кнопку Continue
    wait.until(EC.visibility_of_element_located(
        (By.ID, 'continue')
    )).click()

    # 8. Прочитайте со страницы итоговую стоимость (Total)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    total = driver.find_element(
        By.CSS_SELECTOR, 'div[data-test="total-label"]').text
    total = total.replace("Total: ", "")

    # 9. Закройте браузер
    driver.quit()

    # 10. Проверьте, что итоговая сумма равна $58.29

    assert total == '$58.29'
