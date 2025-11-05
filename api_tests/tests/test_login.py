import allure
from api_tests.utils.api_client import APIClient

BASE_URL = "https://keeping.uz"
LOGIN_ENDPOINT = "/services/platon-auth/api/login"

@allure.title("Login API should authenticate valid user")
@allure.description("Verifies that a user can login successfully and receives a valid token or success response")
def test_login_success():
    client = APIClient(BASE_URL)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "device-id": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }

    data = {
        "username": "user306988371",
        "password": "My4KfWLJ"
    }

    response = client.post(LOGIN_ENDPOINT, data=data, headers=headers)

    # Assertions
    with allure.step("Verify response status"):
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    with allure.step("Verify access token exists"):
        json_data = response.json()
        assert "data" in json_data, "No 'data' key in response"
        assert "access_token" in json_data["data"], "No access token in response"
        assert "refresh_token" in json_data["data"], "No refresh token in response"


