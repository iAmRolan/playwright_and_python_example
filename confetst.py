import pytest
import requests
from playwright.sync_api import sync_playwright
from api.products import create_product

# fetch JWT
@pytest.fixture
def admin_token():
    url = "https://shop.example.com/api/auth/login"
    login_data = {"username": "admin", "password": "admin123"}
    response = requests.post(url, json=login_data)
    return response.json().get("token")


@pytest.fixture
def browser_context():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser_context):
    return browser_context.new_page()


@pytest.fixture
def test_product(admin_token):
    import time
    name = f"TestProduct-{int(time.time())}"
    return create_product(admin_token, name, price=10)
