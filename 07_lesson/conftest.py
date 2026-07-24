import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def firefox_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
