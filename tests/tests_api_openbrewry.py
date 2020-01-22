"""Tests API for openbrewerydb.org service"""
import pytest
import random


def test_status_ok(api_client):
    """Test for status code"""
    response = api_client.get()
    assert response.ok


@pytest.mark.parametrize('by_type', ['micro', 'planning'])
@pytest.mark.parametrize('by_state', ['Ohio', 'california'])
def test_api_type_filtering(api_client, by_type, by_state):
    """Test for filtering response with parameters"""
    response = api_client.get(path='/breweries', params={'by_type': by_type, 'by_state': by_state})
    assert response.json() != []
    assert response.ok


@pytest.mark.parametrize('per_page', [1, 20, 50])
def test_api_per_page(api_client, per_page):
    """Test for compare number of breweries"""
    response = api_client.get(path='/breweries', params={'per_page': per_page})
    assert len(response.json()) == per_page


@pytest.mark.parametrize('single_brew_number', [random.randint(1, 100)])
def test_api_random_id(api_client, single_brew_number):
    """Test for getting a single brewery and compare id"""
    response = api_client.get(path='/breweries' + '/' + str(single_brew_number))
    assert response.json()['id'] == single_brew_number


@pytest.mark.parametrize('query', ['dog', 'cat', 'bird'])
def test_api_search_query(api_client, query):
    """Test for search breweries based on a search term."""
    response = api_client.get(path='/breweries/search', params={'query': query})
    assert query in response.text
