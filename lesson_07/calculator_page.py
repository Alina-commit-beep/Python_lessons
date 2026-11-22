from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = ("https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html")

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, symbol):
        locator = (By.XPATH, f"//span[text()='{symbol}']")
        self.driver.find_element(*locator).click()

    def calculate(self, *symbols):
        for symbol in symbols:
            self.click_button(symbol)

    def wait_for_result(self, expected, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, str(expected))
        )

    def get_result(self):
        return self.driver.find_element(*self.SCREEN).text
