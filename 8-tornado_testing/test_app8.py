"""Example tornado-app test, test requests to url in project №8
run by py.test -- py.test 8-tornado_testing/test_app8.py -vs
or unittest from inside of a folder"""
import json
import unittest
from unittest.mock import MagicMock, create_autospec

from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase, gen_test

import app8

app = app8.make_app()


class ApiTestCase(AsyncHTTPTestCase):
    def get_app(self):
        self.app = app
        return self.app

    def test_get(self):
        response = self.fetch("/", method="GET")
        self.assertEqual(response.code, 200)
        assert response.body == b"Hi"

    def test_post(self):
        response = self.fetch(
            "/?login=small",
            method="POST",
            body="",
            follow_redirects=False,
            headers={
                "Content-Type": "application/json; charset=UTF-8",
                "Cookie": "=".join(("cookie_secret", "jhvkv.kjb;bkucthtxgrx")),
            },
        )
        self.assertEqual(response.code, 200)
        assert response.body == b'You wrote {"login": "small"}'

    def test_put(self):
        app8.function_for_test = MagicMock(return_value=True)
        response = self.fetch("/", method="PUT", body="", follow_redirects=False)
        self.assertEqual(response.code, 200)
        assert response.body == b'{"res": true}'


    def test_get_mock(self):
        app8.function2_for_test = MagicMock(return_value=True)
        response = self.fetch("/m", method="GET")
        assert response.body == b'{"res": true}'

    @gen_test
    def test_put_async_mock(self):
        # Mock async_function_for_test:
        app8.async_function_for_test = create_autospec(app8.async_function_for_test, return_value=True)
        
        client = AsyncHTTPClient()
        response = yield client.fetch(self.get_url('/m'), body="", method="PUT")
        assert response.body == b'{"res": true}'

    @gen_test
    async def test_var_mock(self):
        """with await"""
        client = AsyncHTTPClient()
        response = await client.fetch(
            self.get_url('/m'), 
            method="POST",
            body="",
            follow_redirects=True,
            headers= {"Content-Type": 'application/json; charset=UTF-8', 
                      'Cookie': '='.join(('cookie_secret', 'b8b7b66d7e3e406eb404cd7c7e4e3eaf'))}
        )
        assert response.body == b'{"res": "abc"}'


if __name__ == "__main__":
    unittest.main()
