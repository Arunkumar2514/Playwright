from playwright.sync_api import sync_playwright, expect
import re

def test_locators2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        page = browser.new_page()
        
        page.goto("https://demo.playwright.dev/todomvc")

        print("Page is loaded successfully")

        input_box = page.get_by_placeholder("What needs to be done?")
        input_box.fill("Buy groceries")
        input_box.press("Enter")
        input_box.fill("Learn Playwright")
        input_box.press("Enter")
        input_box.fill("Go to the gym")
        input_box.press("Enter")

        page.screenshot(path="TODO.png")

        print(page.locator("li").first.inner_text())
        print(page.locator("li").nth(1).inner_text())
        print(page.locator("li").last.inner_text())


        option=page.locator("li").filter(has_text="Learn Playwright")

        option.locator(".toggle").click()

        expect(option).to_have_class(re.compile("completed"))

        expect(page.locator("li.completed")).to_have_count(1)
        
        print("Task is marked as completed successfully")

        browser.close()

if __name__ == "__main__":
    test_locators2()