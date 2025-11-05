import pytest
import allure
from api_tests.utils.api_client import APIClient

BASE_URL = "https://keeping.uz"
LOGIN_ENDPOINT = "/services/platon-auth/api/login"
BALANCE_SHEET_ENDPOINT = "/services/platon-core/web/v1/pages/balance_sheet"
PRIMARY_DOC_ENDPOINT = "/services/platon-core/web/v1/pages/primary_doc_v2"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "device-id": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

LOGIN_DATA = {
    "username": "user306988371",
    "password": "My4KfWLJ"
}

@pytest.fixture(scope="session")
def access_token():
    """Login once and return access token for all tests in the session"""
    client = APIClient(BASE_URL)
    response = client.post(LOGIN_ENDPOINT, data=LOGIN_DATA, headers=HEADERS)
    assert response.status_code == 200, "Login failed"
    json_data = response.json()
    token = json_data["data"]["access_token"]
    return token

@allure.title("GET Balance Sheet Page")
@allure.description("Verifies that the Balance Sheet page returns 200 and contains expected data")
def test_balance_sheet_page(access_token):
    client = APIClient(BASE_URL)
    auth_headers = {**HEADERS, "Authorization": f"Bearer {access_token}"}

    with allure.step("Send GET request to Balance Sheet endpoint"):
        response = client.get(BALANCE_SHEET_ENDPOINT, headers=auth_headers)
        allure.attach(str(response.status_code), "Status code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

    with allure.step("Verify response status"):
        assert response.status_code == 200

    with allure.step("Verify response content"):
        json_data = response.json()
        assert "data" in json_data, "No 'data' key in response"


@allure.title("GET Primary Document Page")
@allure.description("Verifies that the Primary Document page returns 200 and contains expected data")
def test_primary_doc_page(access_token):
    client = APIClient(BASE_URL)
    auth_headers = {**HEADERS, "Authorization": f"Bearer {access_token}"}

    with allure.step("Send GET request to Primary Document endpoint"):
        response = client.get(PRIMARY_DOC_ENDPOINT, headers=auth_headers)
        allure.attach(str(response.status_code), "Status code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

    with allure.step("Verify response status"):
        assert response.status_code == 200

    with allure.step("Verify response content"):
        json_data = response.json()
        assert "data" in json_data, "No 'data' key in response"
