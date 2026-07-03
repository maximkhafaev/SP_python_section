from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/links/10")
    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9

    for link in links:
        assert link.is_displayed

    assert links[0].text == "1"

    driver.quit()
