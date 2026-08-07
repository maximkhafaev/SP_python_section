from pages.saucedemo_shop_cart_page import DemoShopCartPage
from pages.saucedemo_shop_catalogue_page import DemoShopCataloguePage
from pages.saucedemo_shop_checkout_page import DemoShopCheckoutPage
from pages.saucedemo_shop_login_page import DemoShopLoginPage
import allure


@allure.parent_suite("LESSON_10")
@allure.suite("SHOP")
@allure.title("Тестирование интернет-магазина")
@allure.description("Тестирует полный цикл действий в интернет-магазине: "
                    ""
                    "авторизация, выбор, добавление в корзину, оформление")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(firefox_driver):
    with allure.step("Инициализируем модули для работы со страницами "
                     "интернет-магазина"):
        LoginPage = DemoShopLoginPage(firefox_driver)
        CataloguePage = DemoShopCataloguePage(firefox_driver)
        CartPage = DemoShopCartPage(firefox_driver)
        CheckoutPage = DemoShopCheckoutPage(
            firefox_driver, 'Max', 'Khafaev', '630090')

    LoginPage.open_demo_shop_login_page()
    LoginPage.authorize()

    CataloguePage.add_items_to_cart()
    CataloguePage.go_to_cart()

    CartPage.go_to_checkout()

    CheckoutPage.fill_customer_information()
    CheckoutPage.press_continue()
    total = CheckoutPage.read_total().replace("Total: ", "")

    with allure.step("Проверяем, что сумма заказа равна $58.29"):
        assert total == '$58.29'
