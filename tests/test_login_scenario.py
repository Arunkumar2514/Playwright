from playwright.sync_api import expect,Page

def test_login_scenario(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    expect(page).to_have_title("Test Login | Practice Test Automation")
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page.locator(".post-title")).to_have_text("Logged In Successfully")
    expect(page.locator("text=Log out")).to_be_visible()
    page.click("text=Log out")
    