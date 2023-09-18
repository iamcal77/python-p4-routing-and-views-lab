# server/testing/app_test.py
import pytest
from flask import Flask
from server.app import app

class TestApp:
    def test_root(self):
        '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
        response = app.test_client().get('/')
        assert b'Python Operations with Flask Routing and Views' in response.data

    def test_print_text(self):
        '''displays text of route in browser.'''
        response = app.test_client().get('/print/hello')
        assert response.data.decode() == '<h1>hello</h1>'

    def test_print_text_console(self):
        '''displays text of route in console.'''
        response = app.test_client().get('/print/hello')
        assert response.status_code == 200

    def test_count_range_10(self):
        '''counts through range of parameter in "/count/<parameter" on separate lines.'''
        response = app.test_client().get('/count/10')
        count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10'
        assert response.data.decode() == count

    def test_math_addition(self):
        '''performs addition operation and returns the result.'''
        response = app.test_client().get('/math/5.5/+/2.5')
        assert response.data.decode() == 'Result: 8.0'

    def test_math_subtraction(self):
        '''performs subtraction operation and returns the result.'''
        response = app.test_client().get('/math/10.5/-/5.5')
        assert response.data.decode() == 'Result: 5.0'

    def test_math_multiplication(self):
        '''performs multiplication operation and returns the result.'''
        response = app.test_client().get('/math/4.0/*/3.5')
        assert response.data.decode() == 'Result: 14.0'

    def test_math_division(self):
        '''performs division operation and returns the result.'''
        response = app.test_client().get('/math/8.0/div/2.0')
        assert response.data.decode() == 'Result: 4.0'

    def test_math_modulus(self):
        '''performs modulus operation and returns the result.'''
        response = app.test_client().get('/math/10.0/%/3.0')
        assert response.data.decode() == 'Result: 1.0'
