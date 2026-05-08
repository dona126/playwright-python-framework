class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page):
        self.page = page

        #locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error_msg = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def get_error(self):
        return self.error_msg
    
    def is_login_button_visible(self):
        return self.login_btn
    
    def get_title(self):
        return self.page.title()