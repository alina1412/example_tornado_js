"""Example tornado-app test, test requests to url in project №8
run by py.test -- py.test 8-tornado_testing/test_app8.py -vs
or unittest from inside of a folder"""
import unittest
from unittest.mock import MagicMock

from tornado.testing import AsyncHTTPTestCase

import app8

app8.function_for_test = MagicMock(return_value=True)
app = app8.make_app()


class ApiTestCase(AsyncHTTPTestCase):
    def get_app(self):
        self.app = app
        return self.app

    def test_get(self):
        response = self.fetch("/", method="GET", follow_redirects=False)
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
        response = self.fetch("/", method="PUT", body="", follow_redirects=False)
        self.assertEqual(response.code, 200)
        assert response.body == b'{"res": true}'


if __name__ == "__main__":
    unittest.main()
