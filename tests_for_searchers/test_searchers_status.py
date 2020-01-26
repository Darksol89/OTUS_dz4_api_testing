"""Тест на получение статус кода"""


def test_searchers(get_url, get_status_code):
    assert get_status_code
