from selenium.webdriver.common.by import By


class MainShopPage:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        locator = (By.CSS_SELECTOR, f"#add-to-cart-{product_id}")
        self.driver.find_element(*locator).click()

    def add_products(self, *product_ids):
        for product_id in product_ids:
            self.add_to_cart(product_id)

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
