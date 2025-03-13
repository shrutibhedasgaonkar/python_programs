from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart(logged_in_driver):
    driver = logged_in_driver
    #driver.get("https://www.saucedemo.com/inventory.html")

    # Assert that we are on the correct page
    assert "inventory.html" in driver.current_url, "User is not on the inventory page!"

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    add_to_cart_button = items[0].find_element(By.CSS_SELECTOR, ".btn_inventory")
    add_to_cart_button.click()

    add_to_cart_button = items[4].find_element(By.CSS_SELECTOR, ".btn_inventory")
    add_to_cart_button.click()

    cart_count = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a > span").text

    # Assert that one item has been added to the cart
    assert cart_count == "2"

    # Navigate to the cart
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()
    assert "cart.html" in driver.current_url








