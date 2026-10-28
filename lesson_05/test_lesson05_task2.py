from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    url_before = driver.current_url

    driver.find_element(By.NAME, "custname").send_keys("Alina")
    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    ).click()

    assert driver.current_url != url_before

    driver.quit()
