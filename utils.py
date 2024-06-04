import os

def get_target_url():
    return os.getenv('TARGET_URL', 'http://example.com')
