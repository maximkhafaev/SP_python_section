# Предварительные шаги
# Создано два аккаунта на https://gitflic.ru/.
# in6vq@airsworld.net 12345Qwerty
# bookend_doyenne3j@icloud.com ryzpov-qyzwen-3gohtI

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://gitflic.ru/.
    driver.get('https://gitflic.ru/')

    # 2. Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZTkzYTU2OWEtNzRmZi00OTRkLTgwMmMtMDA2OTgxZGUxNGEy",
        "domain": "gitflic.ru"
    }
    )
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    }
    )

    # 3. Обновите страницу.
    driver.refresh()

    # 4. Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/project")
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "profile-page__profile-name")
    )).click()

    # 5. Сохраните текущий URL.
    url_user1 = driver.current_url

    # 6. Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()
    driver.get('https://gitflic.ru/')

    # 7. Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZmJkOWY1M2EtMDAyOS00YTY1LTk0MmItYjk5ZWJlNDU1MmZl",
        "domain": "gitflic.ru"
    }
    )
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    }
    )

    # 8. Обновите страницу.
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/project")
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "profile-page__profile-name")
    )).click()

    # 10. Сохраните текущий URL.
    url_user2 = driver.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2

    driver.quit()
