from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    #Valid user logs in. Check URL after logging in.
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page: Page):
    #Invalid user logs in. Gets the error message.
    login = LoginPage(page)
    login.goto()
    login.login("wrong_user", "wrong_pass")
    error = login.get_error()
    expect(error).to_be_visible()
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service")

    
