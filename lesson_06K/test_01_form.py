from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

FIELDS = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro",
}


def test_form_validation():
    # Windows: Edge. На macOS замените на webdriver.Safari()
    driver = webdriver.Edge()
    try:
        driver.maximize_window()
        driver.get(URL)
        wait = WebDriverWait(driver, 10)

        for field_id, value in FIELDS.items():
            field = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, f"[name='{field_id}']")
                )
            )
            field.send_keys(value)

        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Ждём, пока Zip code получит красную подсветку
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#zip-code.alert-danger")
            )
        )
        zip_class = driver.find_element(
            By.CSS_SELECTOR, "#zip-code"
        ).get_attribute("class")
        assert "alert-danger" in zip_class

        for field_id in FIELDS:
            css_class = driver.find_element(
                By.CSS_SELECTOR, f"#{field_id}"
            ).get_attribute("class")
            assert "alert-success" in css_class, field_id
    finally:
        driver.quit()
