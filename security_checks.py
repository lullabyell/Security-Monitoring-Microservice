import requests
import utils

def check_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url, params={"q": payload})
    if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
        return {"check": "SQL Injection", "status": "vulnerable"}
    return {"check": "SQL Injection", "status": "secure"}

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={"q": payload})
    if payload in response.text:
        return {"check": "XSS", "status": "vulnerable"}
    return {"check": "XSS", "status": "secure"}

def run_security_checks():
    url = utils.get_target_url()
    results = []
    results.append(check_sql_injection(url))
    results.append(check_xss(url))
    return results
