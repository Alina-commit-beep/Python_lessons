from selenium import webdriver

from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)
        page.calculate("7", "+", "8", "=")
        page.wait_for_result("15", timeout=50)

        assert page.get_result() == "15"
    finally:
        driver.quit()
