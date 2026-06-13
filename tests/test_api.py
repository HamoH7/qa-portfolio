import requests

BASE_URL = "https://automationexercise.com/api"


class TestProductsAPI:

    def test_site_responds(self):
        response = requests.get(f"{BASE_URL}/productsList")
        assert response.status_code == 200

    def test_products_list_is_not_empty(self):
        response = requests.get(f"{BASE_URL}/productsList")
        data = response.json()
        assert len(data["products"]) > 0