from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")

    driver.find_element(By.CSS_SELECTOR, 'a[href="/forms/post"]').click()
    assert driver.current_url == "https://httpbin.org/forms/post"

    driver.back()
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
