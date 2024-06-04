import pytest
import requests_mock

@pytest.fixture
def requests_mock():
    with requests_mock.Mocker() as mocker:
        yield mocker
