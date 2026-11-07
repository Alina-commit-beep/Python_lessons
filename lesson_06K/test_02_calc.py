from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get(URL)

        delay = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay.clear()
        delay.send_keys("45")

        for key in ("7", "+", "8", "="):
            driver.find_element(
                By.XPATH, f"//span[text()='{key}']"
            ).click()

        screen = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(screen, "15")
        )
        assert driver.find_element(*screen).text == "15"
    finally:
        driver.quit()
