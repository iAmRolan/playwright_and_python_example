from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = "checkout button"
        self.cart_item_name = "item name"

    def open(self):
        self.page.goto("https://shop.example.com/cart")

    def get_item_name(self):
        return self.page.inner_text(self.cart_item_name)

    def go_to_checkout(self):
        self.page.click(self.checkout_button)
