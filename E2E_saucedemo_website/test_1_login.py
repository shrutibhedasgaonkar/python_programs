def test_valid_login(logged_in_driver):
    # Assert successful login by checking URL or page element
    assert "inventory.html" in logged_in_driver.current_url
