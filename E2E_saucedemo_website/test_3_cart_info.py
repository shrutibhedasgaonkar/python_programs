from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_cart_info(logged_in_driver):

    driver = logged_in_driver
    #driver.get("https://www.saucedemo.com/cart.html")

    # Assert we are on the cart page (this assumes navigation from add_to_cart.py)
    assert "cart.html" in driver.current_url, "User is not on the Cart Info page!"

    # Wait for cart items to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))

    # Get all items in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

    # Verify there are 2 items in the cart (as added in add_to_cart.py)
    assert len(cart_items) == 2, f"Expected number of items are 2 but found {len(cart_items)}"

    # Extract details of each item (e.g., name and price)

    item_names = []
    item_prices = []

    for item in cart_items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_price = item.find_element(By.CLASS_NAME, "inventory_item_price").text

        # Append to lists
        item_names.append(item_name)
        item_prices.append(item_price)

    # Print names and prices
    print(f"Items in Cart: {item_names}")
    print(f"Prices of Items: {item_prices}")

    driver.find_element(By.ID, "checkout").click()

    assert "checkout-step-one.html" in driver.current_url, "Failed to navigate to checkout information page!"
















