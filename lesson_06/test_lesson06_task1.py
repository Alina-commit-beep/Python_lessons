from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#finish h4"), "Hello World!"
            )
        )

        driver.save_screenshot("lesson_06/hello_world.png")

        text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
        assert text == "Hello World!"
    finally:
        driver.quit()
