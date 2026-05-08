class ProductsPage:
    def __init__(self, page):
        self.page = page

        #Locators
        # all product items..PARENT div (whole list)
        self.products = page.locator("[data-test='inventory-list']")   

        #Filtering locator of first addable product
        self.first_addable_product = page.locator("[data-test='inventory-item']").filter(
            has=page.get_by_role("button", name="Add to cart")).first
        self.product_name = self.first_addable_product.locator(".inventory_item_name")
        self.add_to_cart_btn = self.first_addable_product.get_by_role("button",name="Add to cart")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")       # cart badge/icon

    def get_product_count(self):
        return self.products.locator("[data-test='inventory-item']").count()
    
    def add_first_item_to_cart(self):
        # get name BEFORE clicking
        name = self.product_name.inner_text()
        print(f"Adding: {name}")
        self.add_to_cart_btn.click()
        return name  # return name we captured before click
    
    def get_cart_count(self):
        return self.cart_icon.inner_text()
    
    def open_cart(self):
        self.cart_icon.click()
