'''tornado test example by AsyncHTTPTestCase
cd 17-tornado_test2 && python3 -m unittest test_1.py '''
import json
import unittest

import tornado
from tornado.testing import AsyncHTTPTestCase
from urllib import parse

from app17 import MainHandler

class MainHandlerTest(AsyncHTTPTestCase):
    def get_app(self):
        return tornado.web.Application([(r"/", MainHandler)])
    
    def test_get(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)
        fake_dict = parse.urlencode({"options" : options_json})

        response = self.fetch(self.get_url('/' + '?' + fake_dict),
                              method="GET", 
                            #   body=f'',
                              )
        self.assertEqual(response.code, 200)

    def test_post_options(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)

        response = self.fetch(self.get_url('/'),
                              method="POST", 
                              body=f'options={options_json}',
                              )

        self.assertEqual(response.code, 200)
        # print(response.body)
        # self.assertEqual(response.body, options_json.encode())

    def test_put_options1(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)

        response = self.fetch(self.get_url('/'),
                              method="PUT", 
                              body=f'options={options_json}',
                              )
        self.assertEqual(response.code, 200)

    def test_put_options2(self):
        options = {'key1': 'value1', 'key2': 'value2'}
        options_json = json.dumps(options)
        fake_body = parse.urlencode({"options" : options_json})

        response = self.fetch(self.get_url('/' + '?' + fake_body), #  + '&additional=7'
                              method="PUT", 
                              body=f'',
                              )
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()
