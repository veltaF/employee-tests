import requests
import pytest
import allure


BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
@allure.step("Create an employee via API")
def create_employee():
    url = f"{BASE_URL}/posts"
    payload = {
        "name": "test6",
        "salary": "123",
        "age": "23"
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Sending POST request to create employee"):
        response = requests.post(url, json=payload, headers=headers)
        allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)


    with allure.step("Validating the response"):
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    return response.json()


@allure.feature("Employee Management API")
@allure.story("Create Employee")
def test_create_employee(create_employee):

    response_body = create_employee

    with allure.step("Checking the response content"):
        assert response_body is not None
        assert "name" in response_body
        assert response_body["name"] == "test6"
        assert response_body["salary"] == "123"
        assert response_body["age"] == "23"
