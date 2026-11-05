import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru/"

USER1 = {
    "cookie": {"name": "SESSION", "value": os.environ["NGYzNzQyMDgtZTZkYS00NjRlLTkzMjItNDJlYmY4Mzk2YTNl"]},
    "profile_url": "https://gitflic.ru/user/lacosta1394",
}
USER2 = {
    "cookie": {"name": "SESSION", "value": os.environ["NTJmN2YwOGItYjk0OC00YzE1LTg2YzEtMTBlZTUxYjU5MmM5"]},
    "profile_url": "https://gitflic.ru/user/chelik1995",
}


def login_and_get_profile_url(driver, user):
    driver.add_cookie(user["cookie"])
    driver.refresh()

    driver.get(user["profile_url"])
    WebDriverWait(driver, 10).until(EC.url_to_be(user["profile_url"]))
    return driver.current_url


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        url_user1 = login_and_get_profile_url(driver, USER1)

        driver.delete_all_cookies()
        driver.get(BASE_URL)

        url_user2 = login_and_get_profile_url(driver, USER2)

        assert url_user1 != url_user2
    finally:
        driver.quit()
