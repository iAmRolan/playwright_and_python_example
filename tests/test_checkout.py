from pages.search_p import SearchPage
from pages.cart_p import CartPage
from api.order import get_order_details

def test_user_can_buy_product(page, test_product, admin_token):
    product_name = test_product["name"]

    search_page = SearchPage(page)
    search_page.open()
    search_page.search(product_name)
    search_page.click_first_product()

    search_page.add_to_cart()

    cart_page = CartPage(page)
    cart_page.open()
    assert product_name in cart_page.get_item_name()

    cart_page.go_to_checkout()
    page.fill("input[name='name']", "Name")
    page.fill("input[name='address']", "B7 4Eva")
    page.click("order button")

    page.wait_for_selector("order id")
    order_id = page.inner_text("order id")

    order_details = get_order_details(admin_token, order_id)
    assert order_details["product_name"] == product_name

    confirmation_text = page.inner_text("confirm order")
    assert product_name in confirmation_text
