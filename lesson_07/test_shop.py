from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from main_shop_page import MainShopPage


def test_shop_total():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        main_page = MainShopPage(driver)
        main_page.add_products(
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie",
        )
        main_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Алина", "Челик", "123456")
        checkout_page.click_continue()
        total = checkout_page.get_total()
    finally:
        driver.quit()

    assert total == "Total: $58.29"
