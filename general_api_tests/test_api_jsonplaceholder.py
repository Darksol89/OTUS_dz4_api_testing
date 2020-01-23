"""Tests for API jsonplaceholder site"""
import pytest
from jsonschema import validate


def test_api_status_code(api_client):
    """Test for status code"""
    response = api_client.get()
    assert response.ok


@pytest.mark.parametrize('valid_userId', [1, 10])
def test_api__valid_filtering(api_client, valid_userId):
    """Test for getting resources with correct ID"""
    response = api_client.get(path='/posts', params={'userId': valid_userId})
    assert response.json() != []


@pytest.mark.parametrize('invalid_userId', [-1, 0, 11])
def test_api_invalid_filtering(api_client, invalid_userId):
    """Test for no getting resources with wrong ID"""
    response = api_client.get(path='/posts', params={'userId': invalid_userId})
    assert response.json() == []


@pytest.mark.parametrize('input_id, output_id',
                         [
                             (101, '101'),
                             (-1, '-1'),
                             (0, '0')
                         ])
@pytest.mark.parametrize('input_body, output_body',
                         [
                             ('test_body', 'test_body'),
                             ('!@#$', '!@#$'),
                             (200, '200')
                         ])
def test_api_create_resource(api_client, input_id, output_id, input_body, output_body):
    """Test with post response for create resource"""
    response = api_client.post(path='/posts',
                               data={'title': 'foo',
                                     'body': input_body,
                                     'userId': input_id}).json()
    assert response['title'] == 'foo'
    assert response['body'] == output_body
    assert response['userId'] == output_id


def test_api_json_schema(api_client):
    """Test with json schema"""
    response = api_client.get(path='/albums/1')

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"},
            "userId": {"type": "number"}
        },
        "required": ["id", "title", "userId"]
    }

    validate(instance=response.json(), schema=schema)
