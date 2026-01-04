import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_google(driver):
    driver.get("https://www.google.com/")

    assert "Google" in driver.title
    assert "google" in driver.current_url


def test_open_github(driver):
    driver.get("https://github.com/")

    assert "GitHub" in driver.title
    assert driver.current_url.startswith("https://github.com/")
