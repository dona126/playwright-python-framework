class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator("[data-test='inventory-item']")    # all product items
        self.first_addable_product = page.locator("[data-test='inventory-list']").filter(
    has=page.get_by_role("button", name="Add to cart")
).first
        self.product_name = self.first_addable_product.locator(".inventory_item_name")
        self.add_to_cart_btn = self.first_addable_product.get_by_role(
    "button",
    name="Add to cart"
)
        self.cart_icon = page.locator("#shopping_cart_container")       # cart badge/icon

    def get_product_count(self):
        return self.products.count()
    
    def add_first_item_to_cart(self):
        self.add_to_cart_btn.click()
        return self.product_name.inner_text()
    
    def get_cart_count(self):
        return self.cart_icon.inner_text()
    
    def open_cart(self):
        self.cart_icon.click()
