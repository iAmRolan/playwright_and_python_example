import requests

def get_order_details(admin_token, order_id):
    url = "https://shop.example.com/api/orders"
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {"order_id": order_id}
    order_response = requests.post(url, json=data, headers=headers)
    return order_response.json()
