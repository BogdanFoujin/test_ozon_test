import requests
import pytest

@pytest.fixture()
def url():
    url = 'https://httpbin.org/get'
    return url

def test_get(url):
    response = requests.get(url)
    assert response.json()['url'] == 'https://httpbin.org/get'