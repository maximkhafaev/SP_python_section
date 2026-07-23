from pages.saucedemo_shop_cart_page import DemoShopCartPage
from pages.saucedemo_shop_catalogue_page import DemoShopCataloguePage
from pages.saucedemo_shop_checkout_page import DemoShopCheckoutPage
from pages.saucedemo_shop_login_page import DemoShopLoginPage


def test_shop(firefox_driver):
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

    assert total == '$58.29'
