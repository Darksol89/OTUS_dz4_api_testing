import pytest
import requests
import json

# main_page_url = 'https://dog.ceo/dog-api/'
# breed_list_url = 'https://dog.ceo/api/breeds/list/all'

def test_check_status_code(api_client):
    response = api_client.get()
    status_code = response.status_code
    assert status_code == 200

def test_json_not_empty(api_client):
    response = api_client.get(path='/breeds/image/random')
    assert response.json() != []


def test_encoding():
    response = requests.get(main_page_url)
    encoding = response.encoding

    assert encoding in 'UTF-8'

def test_text():
    response = requests.get(main_page_url)
    text_list = response.links
    print(text_list)