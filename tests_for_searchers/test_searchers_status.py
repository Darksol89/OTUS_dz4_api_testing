"""Тест на получение кодировки выбранного поисковика"""


def test_searchers(get_url, get_status_code):
    print(get_url.encoding)
    print('\nTest finished')
