from playwright.sync_api import sync_playwright, expect

def test_locators():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        page = browser.new_page()
        
        page.goto("https://demo.playwright.dev/todomvc")

        print("Page is loaded successfully")

        input_box = page.get_by_placeholder("What needs to be done?")
        input_box.fill("Buy groceries")
        input_box.press("Enter")
        input_box.fill("test data")
        input_box.press("Enter")

        page.screenshot(path="TODO.png")

        expect(page.get_by_text("Buy groceries")).to_be_visible()
        expect(page.get_by_text("TestData")).to_be_visible()
        
        print("Task is added successfully")

        browser.close()

if __name__ == "__main__":
    test_locators()

        