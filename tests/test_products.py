from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_products_load(page: Page):
    #Verify products are displayed and assert if 6 products are displayed
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    products = ProductsPage(page)
    assert products.get_product_count() == 6
    
    
    
def test_add_to_cart(page: Page):
    #Verify add to cart of first item and checks if item got added in cart
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    products = ProductsPage(page)
    productN_added_to_cart = products.add_first_item_to_cart()
    products.open_cart()
    cart = CartPage(page)
    all_items_in_cart = cart.check_item_in_cart()
    expect(all_items_in_cart).to_contain_text(productN_added_to_cart)
    