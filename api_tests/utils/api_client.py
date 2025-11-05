import requests
import allure
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    @allure.step("POST {endpoint}")
    def post(self, endpoint, data=None, headers=None, json_data=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        allure.attach(
            json.dumps({
                "url": url,
                "headers": headers,
                "data": data or json_data
            }, indent=2),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )
        response = self.session.post(url, data=data, headers=headers)
        self._attach_response(response)
        return response
    def get(self, endpoint: str, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        allure.attach(
            json.dumps({
                "url": url,
                "params": params,
                "headers": headers
            }, indent=2),
            name="Request",
            attachment_type=allure.attachment_type.JSON
        )
        response = self.session.get(url, params=params, headers=headers)
        self._attach_response(response)
        return response

    def _attach_response(self, response):
        """Attach detailed response info to Allure report."""
        try:
            content = response.json()
        except Exception:
            content = response.text
        allure.attach(
            json.dumps({
                "status_code": response.status_code,
                "elapsed_ms": response.elapsed.total_seconds() * 1000,
                "body": content
            }, indent=2, ensure_ascii=False),
            name="Response",
            attachment_type=allure.attachment_type.JSON
        )

