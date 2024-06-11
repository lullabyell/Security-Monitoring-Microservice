# Security Monitoring Microservice

This project is a security monitoring microservice. The microservice performs basic security checks such as SQL injection and XSS detection.

## Installation

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set the target URL environment variable (optional):
    ```bash
    export TARGET_URL=http://example.com
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Access the endpoints:
    - Health check: `http://localhost:5000/health`
    - Security checks: `http://localhost:5000/check_security`

## Running Tests

Run the tests using pytest:
```bash
pytest tests/
