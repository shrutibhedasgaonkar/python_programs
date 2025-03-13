import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def web_driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver_browser = webdriver.Chrome()
    driver_browser.maximize_window()
    yield driver_browser


def login(web_driver):
    web_driver.get("https://www.saucedemo.com/")

    # Wait for username field to be visible
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    # Enter valid credentials and login
    web_driver.find_element(By.ID, "user-name").send_keys("standard_user")
    web_driver.find_element(By.ID, "password").send_keys("secret_sauce")
    web_driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page to load
    WebDriverWait(web_driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in web_driver.current_url

    # Verify the products are there
    products = web_driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No products found after login!"


@pytest.fixture(scope="session")
def logged_in_driver(web_driver):
    login(web_driver)
    yield web_driver




