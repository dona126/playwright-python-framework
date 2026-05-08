class CartPage:
    def __init__(self, page):
        self.page = page
        self.products_in_cart = page.locator("[data-test='cart-desc-label']")  
    
    def check_item_in_cart(self):
        return self.products_in_cart

         
