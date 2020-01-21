"""Тесты для API на сайте про собак"""
import pytest
from jsonschema import validate


@pytest.mark.parametrize('status', ['200'])
def test_api_status_code(api_client, status):
    """Тест на возвращение статус кода 200"""
    response = api_client.get()
    status_code = response.status_code
    assert status_code == int(status)


def test_api_json_not_empty(api_client):
    """Тест что json не пустой"""
    response = api_client.get(path='/breeds/image/random')
    assert response.json() != []


@pytest.mark.parametrize('status', ['error'])
@pytest.mark.parametrize('message', ['No route found for \"POST /api/status/404\" with code: 0'])
@pytest.mark.parametrize('code', ['404'])
def test_api_post_request(api_client, status, message, code):
    """Тест на ошибку 404"""
    response = api_client.post(path='/status/404',
                               data={'status': status,
                                     'message': message,
                                     'code': code}).json()

    assert response['status'] == status
    assert response['message'] == message
    assert response['code'] == int(code)


@pytest.mark.parametrize('coding', ['UTF-8'])
def test_api_encoding(api_client, coding):
    """Тест на проверку кодировки"""
    response = api_client.get()
    assert response.encoding in coding


def test_api_json_scheme(api_client):
    """Тест с использованием json схемы"""
    response = api_client.get('/breeds/image/random')
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    validate(instance=response.json(), schema=schema)
