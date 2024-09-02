import requests

import pytest
import time 
import allure
from modules.employee import create_employee 
from modules.utils import create_unique_name
from modules.utils import proxy_request 
from data.common import BASE_URL, HEADERS


@allure.suite("Employee Management Suite")
class TestEmployeeManagement:

    @allure.title("Test to create new employee")
    def test_create_employee(self):

        with allure.step("Create new employee"):
            name = create_unique_name()
            response_body = create_employee(name)

        with allure.step("Check employee is created"):
            assert response_body is not None
        
        with allure.step("Check employee data"):
            employee_data = response_body["data"]
            assert employee_data["name"] == name
            assert employee_data["salary"] == "123"
            assert employee_data["age"] == "23"


    @allure.title("Test to fetch employee by id")
    def test_fetch_employee(self):

        employee_id = "7120"

        with allure.step("Send POST request to create new employee"):
            response = proxy_request('GET', BASE_URL, f'/employee/{employee_id}', {'headers': HEADERS})

        print(f"Fetch Response Status Code: {response.status_code}")
        print(f"Fetch Response Headers: {response.headers}")
        print(f"Fetch Response Body: {response.text}")


        with allure.step("Check response"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
            response_json = response.json()
        
            assert response_json['status'] == 'success'
            assert response_json['data'] is None
            assert response_json['message'] == 'Successfully! Record has been fetched.'    