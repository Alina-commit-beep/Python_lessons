from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com/"

ITEMS = (
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-onesie",
)


def test_shop_total():
    driver = webdriver.Firefox()
    total_text = ""
    try:
        driver.maximize_window()
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        for item_id in ITEMS:
            wait.until(
                EC.element_to_be_clickable((By.ID, item_id))
            ).click()

        driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        ).click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Алина")
        driver.find_element(By.ID, "last-name").send_keys("Челик")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        total_text = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        ).text
    finally:
        driver.quit()

    assert total_text == "Total: $58.29"
