from playwright.sync_api import sync_playwright,expect
import re

def test_assertions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        page=browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc")

        expect(page).to_have_url(re.compile("todomvc"))

        expect(page).to_have_title(re.compile("TodoMVC"))