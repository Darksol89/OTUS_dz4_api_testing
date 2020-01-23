"""Фикстуры для выбора необходимого линка, через коммандную строку"""
import pytest
import requests

url_dog_ceo = 'https://dog.ceo/api'
url_openbrewry = 'https://api.openbrewerydb.org'
url_json_placeholder = 'https://jsonplaceholder.typicode.com'


class APIClient:
    """Клиент для рабоыт с API.
    Анализирует выбранный линк куда посылать запросы"""

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print('POST request to {}'.format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path='/', params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    """Парсер для выбора целевого линка до старта теста"""
    parser.addoption('--url',
                     action='store',
                     default='https://api.openbrewerydb.org',
                     help='Target link for request')


@pytest.fixture(scope='session')
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
