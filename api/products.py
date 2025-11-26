import requests

def create_product(admin_token, name, price):
    url = "https://shop.example.com/api/products"
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {"name": name, "price": price}
    product_response = requests.post(url, json=payload, headers=headers)
    return product_response.json()
