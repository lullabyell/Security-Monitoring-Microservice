import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import security_checks

def test_check_sql_injection_vulnerable(requests_mock):
    url = 'http://example.com'
    requests_mock.get(f"{url}?q=' OR '1'='1", text="syntax error")
    result = security_checks.check_sql_injection(url)
    assert result['status'] == 'vulnerable'

def test_check_sql_injection_secure(requests_mock):
    url = 'http://example.com'
    requests_mock.get(f"{url}?q=' OR '1'='1", text="No error")
    result = security_checks.check_sql_injection(url)
    assert result['status'] == 'secure'
