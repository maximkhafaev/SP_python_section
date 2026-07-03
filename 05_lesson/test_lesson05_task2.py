from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/forms/post")

    driver.find_element(
        By.CSS_SELECTOR, 'input[name="custname"]').send_keys('Максим Хафаев')
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()
    assert driver.current_url != "https://httpbin.org/forms/post"

    driver.quit()
