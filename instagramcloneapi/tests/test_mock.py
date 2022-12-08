import math

import os

import requests

def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path


def test_get_current_directory(monkeypatch):
    """
    GIVEN a monkeypatched version of os.getcwd()
    WHEN example1() is called
    THEN check the current directory returned
    """
    def mock_getcwd():
        return '/data/user/directory123'

    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert example1() == '/data/user/directory123'


def example2():
    """
    Call GET for http://httpbin.org/get

    Returns:
        Status Code of the HTTP Response
        URL in the Text of the HTTP Response
    """

    r = requests.get('http://httpbin.org/' + 'get')

    if r.status_code == 200:
        response_data = r.json()
        return r.status_code, response_data["url"]
    else:
        return r.status_code, ''


def test_get_response_success(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = 'http://httpbin.org/get'
            self.headers = {
                'blah': '1234'
            }

        def json(self):
            return {
                'account': '5678',
                'url': 'http://www.testurl.com'
            }

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert example2() == (200, 'http://www.testurl.com')
