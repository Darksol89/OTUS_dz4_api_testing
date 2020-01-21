import pytest
import requests
import json

main_page_url = 'https://dog.ceo/dog-api/'
breed_list_url = 'https://dog.ceo/api/breeds/list/all'

def test_check_status_code():
    response = requests.get(main_page_url)
    status_code = response.status_code
    assert status_code == 200

@pytest.mark.parametrize('content_type', ['Content-Type'])
def test_check_headers(content_type):
    response = requests.get(main_page_url)
    header = response.headers[content_type]

    assert header in 'text/html; charset=UTF-8'

def test_encoding():
    response = requests.get(main_page_url)
    encoding = response.encoding

    assert encoding in 'UTF-8'

def test_text():
    response = requests.get(main_page_url)
    text_list = response.links
    print(text_list)