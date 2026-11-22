from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
