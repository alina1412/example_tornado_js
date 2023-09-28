'''tornado test example 
cd 3-tornado_js_post && python3 -m unittest test_2.py '''
import json
import unittest

import tornado
from tornado.testing import AsyncHTTPTestCase

from app3 import MainHandler


class MainHandlerTest(AsyncHTTPTestCase):
    def get_app(self):
        return tornado.web.Application([(r"/main/", MainHandler)], cookie_secret='123')

    def test_post_options(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)

        response = self.fetch('/main/', 
                              method="POST", 
                              body=f'options={options_json}',
                              headers= {'Cookie': '='.join(('session_id', 'session_id'))},
                              )

        self.assertEqual(response.code, 200)
        # print(response.body)
        self.assertEqual(response.body, options_json.encode())


if __name__ == '__main__':
    unittest.main()
