"""Example tornado-app test, test requests to url in project №3
run by py.test or unittest from inside of a folder"""
import json
import unittest

from tornado.testing import AsyncHTTPTestCase

import app3
app = app3.make_app()


class ApiTestCase(AsyncHTTPTestCase):
  def get_app(self):
    self.app = app
    return self.app
  
  def test_post(self):
    post_args = json.dumps({"message": "123"})
    response = self.fetch(
        '/form/',
        method='POST',
        body=post_args,
        follow_redirects=False)
    self.assertEqual(response.code, 200)
    print(response.body)
 

  def test_get(self):
    response = self.fetch(
        '/main/',
        method='GET',
        follow_redirects=False)
    self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()
