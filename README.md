# FEmployee API tests

This project contains tests for the Employee API using Python's `pytest` framework with Allure for reporting.

## Prerequisites

```bash
Python 3.8+
pip
```

## Setup and Running Locally

### On Unix-based Systems

1. **Clone the Repository**

   ```bash
    ghttps://github.com/veltaF/employee-tests.git
    cd employee-tests
    ```
2. **Setup Python Virtual Environment**

    ```bash
    python3 -m venv test_env
    source test_env/bin/activate
    ```
3. **Install Dependencies**

   ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **Running  tests**

   ```bash
    python -m pytest --alluredir allure-results
    ```   

5. **Generate report**
    ```bash
        allure generate --single-file ./allure-results -o ./allure-report
    ``` 

## Continuous Integration

This project uses a GitHub Actions workflow that automatically runs tests and generates an Allure report whenever new changes are pushed to the repository. The Allure report is stored as an artifact, which you can download and view after the workflow completes.

You can find the workflow configuration in the `.github/workflows` directory of this repository.
