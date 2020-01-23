"""Фикстуры для получение ссылки и кода состояние из
параметров коммандной строки."""
import requests
import pytest


def pytest_addoption(parser):
    """Парсеры добавления параметров - код состояния и ссылка"""
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help="Link for checking status code")
    parser.addoption('--status_code',
                     action='store',
                     default='200',
                     help='Status code for http response')


@pytest.fixture()
def get_url(request):
    """Фикстура получения ссылки из параметра ком.строки"""
    url = request.config.getoption('--url')
    return requests.get(url)


@pytest.fixture()
def get_status_code(request, get_url):
    """Фикстура получения кода состояния из параметра ком.строки"""
    request.config.getoption('--status_code')
    return get_url.status_code
