from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_personal_info(logged_in_driver):
    driver = logged_in_driver
    #driver.get("https://www.saucedemo.com/checkout-step-two.html")

    # Assert that we are on the correct page
    assert "checkout-step-two.html" in driver.current_url, "User failed to navigate to checkout-step-two page"

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

    cart_items_in_checkout = driver.find_elements(By.CLASS_NAME, "cart_item")

    items_names_checkout = []
    items_prices_checkout = []

    for item_checkout in cart_items_in_checkout:
        item_name = item_checkout.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_price = item_checkout.find_element(By.CLASS_NAME, "inventory_item_price").text

        items_names_checkout.append(item_name)
        items_prices_checkout.append(item_price)

        # Example expected data (replace with actual cart data from previous steps)
    expected_item_names = ["Sauce Labs Backpack", "Sauce Labs Onesie"]
    expected_item_prices = ["$29.99", "$7.99"]

    assert items_names_checkout == expected_item_names, (f"Item name does not match. Expected is {expected_item_names},"
                                                         f"Actual is {items_names_checkout}")

    assert items_prices_checkout == expected_item_prices, (f"Item price does not match. Expected is "
                                                           f"{expected_item_prices}, Actual is {items_prices_checkout}")

    subTotal_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    tax_price = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    subtotal_value = float(subTotal_price.split("$")[1])
    tax_value = float(tax_price.split("$")[1])
    total_value = float(total_price.split("$")[1])
    assert abs(total_value - (subtotal_value + tax_value)) < 0.01

    driver.find_element(By.ID, "finish").click()

    # Verify navigation to final page
    assert "checkout-complete.html" in driver.current_url

    final_message = final_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in final_message, ("Final message is incorrect"
                                                          "")