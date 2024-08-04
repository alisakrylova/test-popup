from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def setup_popup(driver):
    driver.get("https://systeme.io/blog/make-money-home")
    print("Navigated to the page.")

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)
    print("Switched to iframe.")

    yield

    driver.switch_to.default_content()
    print("Switched back to main content after test")


@pytest.mark.usefixtures("setup_popup")
def test_first_button(driver):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button-0a65a969"))
    )
    print("Button is present on the popup.")

    button_text = button.text
    assert button_text == "I want to receive my copy"


@pytest.mark.usefixtures("setup_popup")
def test_second_button(driver):
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-testid="popup-close-icon"]')
        )
    )
    print("Close button is present on the popup and clickable.")

    sleep(5)

    close_button.click()
    print("Close Button clicked.")

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.TAG_NAME, "iframe"))
    )
    print("Iframe is no longer visible.")
