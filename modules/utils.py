import requests
import allure
import pytest
from datetime import datetime

@pytest.fixture(autouse=False)
def slow_down_tests():
    yield
    time.sleep(60)
       

def create_unique_name(base_name = "test"):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{base_name}_{current_time}"

def proxy_request(method, base_url, endpoint, options):
    try:
        api_key = "c4e2edc8caf08aa274be7df48ce7de9c"
        base_proxy_url = 'http://api.scraperapi.com'
        proxy_url = f"{base_proxy_url}?api_key={api_key}&url={requests.utils.quote(base_url + endpoint)}"


        allure.attach(body=f"Method: {method}\nURL: {proxy_url}\nOptions: {options}", 
                    name="Request details", attachment_type=allure.attachment_type.TEXT)


        print(f"Request URL: {proxy_url}")

        if method.upper() == 'POST':
            response = requests.post(proxy_url, **options)
        elif method.upper() == 'GET':
            response = requests.get(proxy_url, **options)    
        elif method.upper() == 'PUT':
            response = requests.put(proxy_url, **options)
        elif method.upper() == 'DELETE':
            response = requests.delete(proxy_url, **options) 
        else:
            raise ValueError(f"Invalid HTTP method: {method}")    
        
        allure.attach(body=response.text, name="Response body", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(response.headers), name="Response headers", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(response.status_code), name="Response status code", attachment_type=allure.attachment_type.TEXT)

        return response

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        allure.attach(body=str(e), name="Unexpected Exception", attachment_type=allure.attachment_type.TEXT)
        raise  # Re-raise the exception after logging and attaching to Allure
    

        