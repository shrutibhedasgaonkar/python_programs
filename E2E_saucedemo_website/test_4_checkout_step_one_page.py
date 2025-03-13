from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_personal_info(logged_in_driver):
    driver = logged_in_driver
    #driver.get("https://www.saucedemo.com/checkout-step-one.html")

    # Assert that we are on the correct page
    assert "checkout-step-one.html" in driver.current_url, "User is not on the Personal_info page!"

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "first-name")))

    # Enter details in the form
    driver.find_element(By.ID, "first-name").send_keys("test1_firstname")
    driver.find_element(By.ID, "last-name").send_keys("test1_lastname")
    driver.find_element(By.ID, "postal-code").send_keys("SM2 1AA")

    driver.find_element(By.CSS_SELECTOR, "input[value = 'Continue']").click()

    # Assert that we are on the correct page
    assert "checkout-step-two.html" in driver.current_url, "User failed to navigate to checkout-step-two page"


