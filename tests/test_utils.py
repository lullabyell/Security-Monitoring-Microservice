import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils

def test_get_target_url_default():
    assert utils.get_target_url() == 'http://example.com'

def test_get_target_url_env_var(monkeypatch):
    monkeypatch.setenv('TARGET_URL', 'http://test.com')
    assert utils.get_target_url() == 'http://test.com'
