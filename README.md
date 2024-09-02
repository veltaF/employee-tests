source test-env/bin/activate


pytest -v -s test_employee_api.py


 rm -rf allure-results/*  

python -m pytest --alluredir allure-results

allure serve allure-results