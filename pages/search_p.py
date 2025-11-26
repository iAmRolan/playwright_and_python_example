from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = "input slector"
        self.search_button = "search button"
        self.product_link = "product link"
        self.add_to_cart_button = "add to cart button" 

    def open(self):
        self.page.goto("https://shop.example.com/search")

    def search(self, text):
        self.page.fill(self.search_input, text)
        self.page.click(self.search_button)

    def click_first_product(self):
        self.page.wait_for_selector(self.product_link)
        self.page.click(self.product_link)

    def add_to_cart(self):
        self.page.wait_for_selector(self.add_to_cart_button)
        self.page.click(self.add_to_cart_button)
