import allure
from data.common import BASE_URL, HEADERS
from modules.utils import proxy_request 
import random


def create_employee(name = "test", salary = "123", age = "23"):
    url = f"{BASE_URL}/create"
    payload = {
        "name": name,
        "salary": salary,
        "age": age
    }

    with allure.step("Send POST request to create new employee"):
        response = proxy_request('POST', BASE_URL, '/create', {'json': payload, 'headers': HEADERS})

    with allure.step("Verify the response status code is 200 OK"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    return response.json()