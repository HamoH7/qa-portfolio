import requests

BASE_URL = "https://automationexercise.com/api"


class TestProductsAPI:

    def test_site_responds(self):
        response = requests.get(f"{BASE_URL}/productsList")
        assert response.status_code == 200