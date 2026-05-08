from playwright.sync_api import Page, expect
import pages.login_page

def test_login_button_visible(page : Page):
    #Checks Login button is visible in Login Page
    login = pages.login_page.LoginPage(page)
    login.goto()
    expect(login.is_login_button_visible()).to_be_visible()


def test_get_page_title(page : Page):
    #Verify the title and prints it, of Login Page
    login = pages.login_page.LoginPage(page)
    login.goto()
    expect(page).to_have_title("Swag Labs")



