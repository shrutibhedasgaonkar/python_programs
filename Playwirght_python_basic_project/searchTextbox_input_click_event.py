from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com")
    page.click("text='Accept all'")
    page.fill("#APjFqb", "Selenium")
    page.press("input[type='submit']", "Enter")

    title = page.title()
    print(title)



    x = input("Press Enter to exit")

